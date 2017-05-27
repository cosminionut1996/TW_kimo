package com.fii.dao;

import java.util.List;
import java.util.stream.Stream;

import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;
import org.springframework.data.repository.query.Param;

import com.fii.model.UserTable;

public interface UserRepository extends CrudRepository<UserTable, Long> {
	
	List<UserTable>findByEmail(String email);
	
	@Query("select c from UserTable c where c.email = :email")
    Stream<UserTable> findByEmailReturnStream(@Param("email") String email);

}
