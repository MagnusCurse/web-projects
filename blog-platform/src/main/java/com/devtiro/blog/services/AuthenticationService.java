package com.devtiro.blog.services;

import com.devtiro.blog.domain.dtos.RegisterRequest;
import com.devtiro.blog.domain.entities.User;
import org.springframework.security.core.userdetails.UserDetails;

public interface AuthenticationService {
    UserDetails authenticate(String email, String password);
    String generateToken(UserDetails userDetails);
    UserDetails validateToken(String token);
    User register(RegisterRequest registerRequest);
}
