import { Injectable } from '@angular/core';
import axios from 'axios';

@Injectable({
  providedIn: 'root',
})
export class Api {

  baseUrl = 'http://127.0.0.1:8000';

  constructor() { }

  // UPLOAD PDF

  async uploadFile(file: File): Promise<any> {
    const formData = new FormData();
    formData.append('file', file);

    const response = await axios.post(
      `${this.baseUrl}/qa/upload`,
      formData,
      {
        headers: { 'Content-Type': 'multipart/form-data' },
      }
    );

    return response.data;
  }


  // ASK QUESTION
  async askQuestion(question: string): Promise<any> {
    const response = await axios.post(
      `${this.baseUrl}/qa/ask`,
      { question }
    );

    return response.data;
  }
}