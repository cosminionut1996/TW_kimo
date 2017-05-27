package com.fii.controller;

import java.util.UUID;

import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import com.fii.model.UserTable;
import com.fii.service.CacheService;
import com.fii.service.UserService;

@Controller
@RequestMapping("/login")
public class LoginController {

	@Autowired
	UserService userService;
	
	@Autowired
	CacheService cacheService;

	@RequestMapping(method = RequestMethod.GET)
	public String displayLoginPage(Model model) {
		UserTable user = new UserTable();
		model.addAttribute("user", user);
		return "login";
	}

	@RequestMapping(method = RequestMethod.POST)
	public String executeLogin(@ModelAttribute UserTable userTable, HttpSession session) {
		if (userService.userExistsInDB(userTable)) {
			cacheService.getLoggedInUsers().put(UUID.randomUUID().toString(),userTable);
			return "home";
		}

		return "redirect:/login";
	}
}
