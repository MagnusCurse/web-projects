package com.devtiro.blog.repositories;

import com.devtiro.blog.domain.entities.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;
import java.util.UUID;

@Repository // Marks this interface as a Spring repository, enabling component scanning and exception translation
public interface UserRepository extends JpaRepository<User, UUID> {
    // This interface extends JpaRepository, which provides standard CRUD (Create, Read, Update, Delete)
    // and pagination/sorting operations out-of-the-box for the User entity.
    // - 'User': The entity type this repository manages.
    // - 'UUID': The type of the primary key for the User entity.

    /**
     * Custom method to find a User by their email address.
     * Spring Data JPA automatically generates the query for this method based on its name.
     * @param email The email address to search for.
     * @return An Optional containing the User if found, or an empty Optional if not found.
     */
    Optional<User> findByEmail(String email);

}
