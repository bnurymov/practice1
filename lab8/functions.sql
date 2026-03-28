-- ============================================================
-- Practice 8: PostgreSQL FUNCTIONS
-- PhoneBook application
-- ============================================================

-- Make sure the contacts table exists
CREATE TABLE IF NOT EXISTS contacts (
    id      SERIAL PRIMARY KEY,
    name    VARCHAR(100) NOT NULL,
    phone   VARCHAR(20)  NOT NULL
);

-- ============================================================
-- FUNCTION 1: Search contacts by pattern
-- Returns all records where name OR phone matches the pattern
-- Usage: SELECT * FROM get_contacts_by_pattern('Ali');
-- ============================================================
CREATE OR REPLACE FUNCTION get_contacts_by_pattern(p TEXT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
        SELECT c.id, c.name, c.phone
        FROM contacts c
        WHERE c.name  ILIKE '%' || p || '%'
           OR c.phone ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;


-- ============================================================
-- FUNCTION 2: Get contacts with pagination
-- Returns contacts using LIMIT and OFFSET
-- Usage: SELECT * FROM get_contacts_paginated(10, 0);
-- ============================================================
CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
        SELECT c.id, c.name, c.phone
        FROM contacts c
        ORDER BY c.name
        LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;
