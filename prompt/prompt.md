
# Command.java

```java
//=======================================
// 이름 : Command.java
// 이 코드의 역할 : Command 인터페이스는 HTTP 요청과 응답을 처리하는 공통 메서드를 정의합니다.
//=======================================
package service;

import java.io.IOException;


import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public interface Command {
	
	void doCommand(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException, Exception;
	
}
```
