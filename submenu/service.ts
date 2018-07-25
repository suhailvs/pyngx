import { Injectable } from '@angular/core';
import { HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class {{ submenu|title }}Service {

  constructor(private  httpClient:  HttpClient) {}

  get{{ submenu|title }}s() {
    return this.httpClient.get('/{{ menu }}/{{ submenu }}/');
  }
  get{{ submenu|title }}(id) {
    return this.httpClient.get(`/{{ menu }}/{{ submenu }}/${id}/`);
  }
  post{{ submenu|title }}({{ submenu }}) {
    return this.httpClient.post('/{{ menu }}/{{ submenu }}/', {{ submenu }});
  }
  update{{ submenu|title }}(id, {{ submenu }}) {
    return this.httpClient.patch(`/{{ menu }}/{{ submenu }}/${id}/`, {{ submenu }});
  }
}
