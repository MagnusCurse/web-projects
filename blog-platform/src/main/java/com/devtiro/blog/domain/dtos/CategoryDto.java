package com.devtiro.blog.domain.dtos;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.UUID;

// The CategoryDto class is a Data Transfer Object (DTO).
// Its primary purpose is to transfer data between different layers of an application,
// or between the application and an external client (like a web browser or another service).
// Contains a subset of fields from the entity, or aggregated/transformed data. Can omit sensitive data or include calculated fields.

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class CategoryDto {
    private UUID id;
    private String name;
    private long postCount;
}
