"""
간단하게 말하면 HTTP protocol로 동신하는 client와 server로 개발하는 거 ..
web client and web server를 같이 개발할 수 있고
web client or web server 하나만 개발할 수 있다
웹 클라이언트가 요청하고 웹서버가 응답하는 클라이언트 서버프로그램이 동작하는거임
web server == web framework 랑은 다르다

web browser 는 (나는 chrome) 주소창에 입력받은 문장을 해석하면 웹서버 한테 http(s) 
요청을 보내는 web client 역할을 수행한다 요청받은 (https://www.example.com) 이라는 도메인을 웹서버는 

그 결과를 chrome 에 전송을 해준다 전송받은 웹 브라우저는 html를 해석을 해서 화면을 보여준다

Linux curl 명령
사용법은 curl https://example.com
리눅스 curl명령은 http/https/ftp 등등 프로토콜을 사용해서 데이터를 송수신
할수 있는 명령어

웹 브라이저에서 보았던 문장이랑 동일하게 나오는 걸 알 수 가 있다
즉, 어떤 방법을 쓰더라도 상관없이 웹서버는 동일함 요청을 받을 때 동일한 응
답을 주고 있는걸 확인할 수 있음

linux telnet
telnet을 이용해서 http 요청을 보낼수 있음

중요한거!!
반드시 웹브라우저가 아니더라도 웹 클라이언트의 요청을 보낼 수 있다.
http(hypertext transfer protocol)는 웹 서버와 웹 클라이온트 사이에서 
데이터를 주고받기 위해 사용하는 통신 방식으로 tcp/ip 프로토콩 위해서 동작한다.. 

즉 우리가 웹을 이용하려면 웹서버와 웹 클라이언트는 각각 tcp/ip 동작에
필수적인 ip주소를 가져와야한다..
"""