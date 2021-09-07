import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Autores } from '../models/autores.model';

@Injectable({
  providedIn: 'root'
})
export class AutorService {
  apiUrl = 'http://127.0.0.1:8000/artigos/autor/'
  constructor(private http:HttpClient) { }

  getAutores(){
    return this.http.get<Autores[]>(this.apiUrl)
  }
}
