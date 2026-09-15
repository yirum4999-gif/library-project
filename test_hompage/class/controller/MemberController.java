package controller;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class LoginController
 */
@WebServlet("/login/*")
public class MemberController extends HttpServlet {
	private static final long serialVersionUID = 1L;

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        doAction(request, response);
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        doAction(request, response);
    }

    protected void doAction(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        request.setCharacterEncoding("utf-8");
        
        String action = request.getPathInfo();
        String page = null;
        
        if (action == null) {
            action = "/login";   // 기본값
        }
        
        switch (action) {
        case "/login":
            page = "/WEB-INF/views/member/login.jsp";
            break;

        case "/register":
            page = "/WEB-INF/views/member/register.jsp";
            break;

        default:
            response.sendError(HttpServletResponse.SC_NOT_FOUND);
            return;
	    }
	
	    request.getRequestDispatcher(page).forward(request, response);
	        
	    }  


}
