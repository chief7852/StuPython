package kr.ncs.web;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;


@WebServlet("/secret")
public class MySecret extends HttpServlet {
   private static final long serialVersionUID = 1L;
    
   protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
      HttpSession session = request.getSession();
      String user_id = (String) session.getAttribute("user_id");
      
      System.out.println(user_id);
      if(user_id == null) {
//         RequestDispatcher rd = request.getRequestDispatcher("/login.html");
//         rd.forward(request, response);
         response.sendRedirect("login.html");
         return;
      }
      
      RequestDispatcher rd = request.getRequestDispatcher("secret.jsp");
      rd.forward(request, response);
   }

   protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
      // TODO Auto-generated method stub
      doGet(request, response);
   }

}