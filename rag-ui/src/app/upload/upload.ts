import { Component, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Api } from '../services/api';

@Component({
  selector: 'app-upload',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './upload.html',
  styleUrl: './upload.css',
})
export class Upload {

  selectedFiles = signal<File[]>([]);

  loading = signal(false);
  uploading = signal(false);
  showPopup = signal(false);
  popupMessage = signal('');
  question = signal('');
  answer = signal('');
  context = signal<string[]>([]);

  constructor(private api: Api) { }

  onFileChange(event: any) {
    const files = Array.from(event.target.files as FileList) as File[];
    this.selectedFiles.update(prev => [...prev, ...files]);
  }

  removeFile(index: number) {
    this.selectedFiles.update(files => files.filter((_, i) => i !== index));
  }

  async upload() {
    const files = this.selectedFiles();
    if (!files.length) {
      this.popupMessage.set("Please upload at least one PDF");
      this.showPopup.set(true);
      return;
    }

    this.uploading.set(true);

    try {
      for (const file of files) {
        await this.api.uploadFile(file);
      }
    } catch (err) {
      console.error(err);
    } finally {
      this.uploading.set(false);
    }
  }

  async ask() {
    if (!this.selectedFiles().length) {
      this.popupMessage.set("Please upload PDF first");
      this.showPopup.set(true);
      return;
    }

    if (!this.question()) {
      this.popupMessage.set("Please enter a question");
      this.showPopup.set(true);
      return;
    }

    this.loading.set(true);
    this.answer.set('');
    this.context.set([]);

    try {
      const res = await this.api.askQuestion(this.question());

      this.answer.set(res?.data?.answer || '');
      this.context.set(res?.data?.context_used || []);

    } catch (err) {
      console.error(err);
    } finally {
      this.loading.set(false);
    }
  }

  closePopup() {
    this.showPopup.set(false);
  }

  clearQA() {
    this.question.set('');
    this.answer.set('');
    this.context.set([]);
    this.selectedFiles.set([]);
  }
}