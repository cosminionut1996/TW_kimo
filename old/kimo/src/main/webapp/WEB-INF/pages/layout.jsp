<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
<%@ page isELIgnored="false" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib uri="http://tiles.apache.org/tags-tiles" prefix="tiles"%>
 
<html>
 
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<%--     <title><tiles:getAsString name="title" /></title> --%>
    <link href="<c:url value='/static/css/bootstrap.css' />"  rel="stylesheet"></link>
    <link href="<c:url value='/static/css/app.css' />" rel="stylesheet"></link>
</head>
  
<body>
        <section id="header">
           <%--  <tiles:insertAttribute name="header" /> --%>
           <h3>Header smecher</h3>
        </section>
     
        <section id="sidemenu">
            <h3>Meniu smechere</h3>
        </section>
             
        <section id="site-content">
            <tiles:insertAttribute name="body" />
        </section>
         
        <footer id="footer">
           <h3> Footer smechereeee </h3>
        </footer>
</body>
</html>