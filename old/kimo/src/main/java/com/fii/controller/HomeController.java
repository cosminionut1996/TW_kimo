package com.fii.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping()
public class HomeController {

	
	@RequestMapping("/home")
	public String getHomePage(){
		return "home";
	}
	
	
	@RequestMapping("/test")
	public String getBla(){
		return "test";
	}
}
