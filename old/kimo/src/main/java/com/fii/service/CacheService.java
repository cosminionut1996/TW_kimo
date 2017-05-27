package com.fii.service;

import java.util.HashMap;
import java.util.Map;

import org.springframework.stereotype.Service;

import com.fii.model.UserTable;

@Service
public class CacheService {
	Map<String, UserTable>loggedInUsers = new HashMap<>();

	public Map<String, UserTable> getLoggedInUsers() {
		return loggedInUsers;
	}

	public void setLoggedInUsers(Map<String, UserTable> loggedInUsers) {
		this.loggedInUsers = loggedInUsers;
	}

	
}
