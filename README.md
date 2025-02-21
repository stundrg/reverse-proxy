# reverse-proxy
- 성능
- 부하 분산(LB)
- 가상호스트 및 라우팅
## Python Server


```bash
$ python -m http.server 8000 --directory pyweb1 # 8000번은 Defaults 값
$ python -m http.server 8002 --directory pyweb2 
$ python -m http.server --directory blog 8003 # 포트 번호를 뒤에 지정해도 된다고 하심 편하실 대로 
```
## Ngix
- https://ubuntu.com/tutorials/install-and-configure-nginx#2-installing-nginx

```bash
# install
sudo apt install nginx

$ sudo service nginx restart
$ sudo service nginx stop
$ sudo service nginx start
$ sudo service nginx status #-> worker 16ea
$ sudo nginx -t 
```

## nGrinder
> $ java -jar ngrinder-controller-3.5.9-p1.war # 컨트롤러 실행 방법
> $ ./run_agent.sh # Agent 실행 방법

- http://localhost:8000 (admin/admin)
```bash
$ pwd
/home/wsl/app
$ tree -L 2
├── ngrinder-agent
│   ├── lib
│   ├── run_agent.sh
│   ├── run_agent_bg.sh
│   ├── run_agent_internal.sh
│   └── stop_agent.sh
└── ngrinder-controller
    └── ngrinder-controller-3.5.9-p1.war
```
