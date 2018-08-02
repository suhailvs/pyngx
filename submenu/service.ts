import { Injectable } from '@angular/core';
import { HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class {{ submenu|title }}Service {

  constructor(private  httpClient:  HttpClient) {}

  get{{ extra|title }}s() {
    return this.httpClient.get('/{{ menu }}/{{ submenu }}/');
  }
  get{{ extra|title }}(id) {
    return this.httpClient.get(`/{{ menu }}/{{ submenu }}/${id}/`);
  }
  post{{ extra|title }}({{ extra }}) {
    return this.httpClient.post('/{{ menu }}/{{ submenu }}/', {{ extra }});
  }
  update{{ extra|title }}(id, {{ extra }}) {
    return this.httpClient.patch(`/{{ menu }}/{{ submenu }}/${id}/`, {{ extra }});
  }
}
