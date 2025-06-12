package com.devtiro.blog.repositories;

import com.devtiro.blog.domain.entities.Category;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.UUID;

@Repository
public interface CategoryRepository extends JpaRepository<Category, UUID> {
    // @Query annotation allows defining custom JPQL (Java Persistence Query Language) queries.
    // "SELECT c FROM Category c" selects all Category entities.
    // "LEFT JOIN FETCH c.posts" performs a left join on the 'posts' relationship of the Category
    // and *fetches* (eagerly loads) the posts collection. This means when a Category is retrieved,
    // its associated posts are loaded in the same query, preventing separate queries for each category's posts.
    @Query("SELECT c FROM Category c LEFT JOIN FETCH c.posts")
    List<Category> findAllWithPostCount();

    boolean existsByNameIgnoreCase(String name);

}
