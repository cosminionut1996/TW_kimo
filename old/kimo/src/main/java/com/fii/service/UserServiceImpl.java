package com.fii.service;

import java.util.HashMap;
import java.util.Map;

import org.springframework.stereotype.Service;

import com.fii.model.UserTable;

@Service
public class UserServiceImpl implements UserService {

	@Override
	public boolean userExistsInDB(UserTable userTable){
		//check user in db
		return true;
	}
}
