package com.fii;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import com.fii.dao.UserRepository;

@Controller
@EnableAutoConfiguration
@SpringBootApplication

public class Application /*implements CommandLineRunner*/ {
	
	public static void main(String[] args) {
		SpringApplication.run(Application.class, args);
	}
	@Autowired
	UserRepository userRepository;


//	@Transactional(readOnly = true)
//	@Override
//	public void run(String... args) throws Exception {
//
//		System.out.println("DATASOURCE = " + dataSource);
//
//		System.out.println("\n1.findAll()...");
//		for (UserTable user : userRepository.findAll()) {
//			System.out.println(user);
//		}
//
//		System.out.println("\n2.findByEmail(String email)...");
//		for (UserTable user : userRepository.findByEmail("asdy@gmail.com")) {
//			System.out.println(user);
//		}
//
////		System.out.println("\n3.findByDate(Date date)...");
////		for (User user : userRepository.findByDate(sdf.parse("2017-02-12"))) {
////			System.out.println(user);
////		}
//
//		// For Stream, need @Transactional
//		System.out.println("\n4.findByEmailReturnStream(@Param(\"email\") String email)...");
//		try (Stream<UserTable> stream = userRepository.findByEmailReturnStream("asdy@gmail.com")) {
//			stream.forEach(x -> System.out.println(x));
//		}
//
//		System.out.println("Done!");
//
//
//	
//	}
}
