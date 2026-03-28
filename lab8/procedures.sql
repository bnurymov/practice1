-- ============================================================
-- Practice 8: PostgreSQL STORED PROCEDURES
-- PhoneBook application
-- ============================================================

-- ============================================================
-- PROCEDURE 1: Upsert a single contact
-- If name already exists → update phone
-- If name does not exist → insert new record
-- Usage: CALL upsert_contact('Alice', '+77001234567');
-- ============================================================
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts
        SET phone = p_phone
        WHERE name = p_name;
        RAISE NOTICE 'Updated phone for "%"', p_name;
    ELSE
        INSERT INTO contacts(name, phone) VALUES (p_name, p_phone);
        RAISE NOTICE 'Inserted new contact "%"', p_name;
    END IF;
END;
$$;


-- ============================================================
-- PROCEDURE 2: Insert many contacts from arrays
-- Validates phone format (must start with + and have 10-15 digits)
-- Returns invalid entries via a temp table
-- Usage: CALL insert_many_contacts(ARRAY['Alice','Bob'], ARRAY['+77001234567','bad']);
-- ============================================================
CREATE OR REPLACE PROCEDURE insert_many_contacts(
    p_names  VARCHAR[],
    p_phones VARCHAR[]
)
LANGUAGE plpgsql AS $$
DECLARE
    i        INT;
    v_name   VARCHAR;
    v_phone  VARCHAR;
BEGIN
    -- Temporary table to collect invalid rows (visible in session)
    DROP TABLE IF EXISTS invalid_contacts;
    CREATE TEMP TABLE invalid_contacts (
        name  VARCHAR,
        phone VARCHAR,
        reason VARCHAR
    );

    FOR i IN 1 .. array_length(p_names, 1) LOOP
        v_name  := p_names[i];
        v_phone := p_phones[i];

        -- Validate: phone must match +XXXXXXXXXX (10-15 digits)
        IF v_phone !~ '^\+[0-9]{10,15}$' THEN
            INSERT INTO invalid_contacts(name, phone, reason)
            VALUES (v_name, v_phone, 'Invalid phone format');
            RAISE NOTICE 'Skipped "%" — invalid phone: %', v_name, v_phone;
            CONTINUE;
        END IF;

        -- Upsert valid contact
        CALL upsert_contact(v_name, v_phone);
    END LOOP;

    RAISE NOTICE 'Batch insert complete. Check "invalid_contacts" table for errors.';
END;
$$;


-- ============================================================
-- PROCEDURE 3: Delete contact by name OR phone
-- Usage: CALL delete_contact('Alice', NULL);
--        CALL delete_contact(NULL, '+77001234567');
-- ============================================================
CREATE OR REPLACE PROCEDURE delete_contact(p_name VARCHAR DEFAULT NULL,
                                           p_phone VARCHAR DEFAULT NULL)
LANGUAGE plpgsql AS $$
DECLARE
    rows_deleted INT;
BEGIN
    IF p_name IS NULL AND p_phone IS NULL THEN
        RAISE EXCEPTION 'Provide at least a name or a phone number to delete.';
    END IF;

    DELETE FROM contacts
    WHERE (p_name  IS NOT NULL AND name  = p_name)
       OR (p_phone IS NOT NULL AND phone = p_phone);

    GET DIAGNOSTICS rows_deleted = ROW_COUNT;
    RAISE NOTICE 'Deleted % row(s).', rows_deleted;
END;
$$;
