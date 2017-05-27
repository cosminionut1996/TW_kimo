package com.fii.service;

import com.fii.model.UserTable;

public interface UserService {
	
	boolean userExistsInDB(UserTable userTable);
	
}
