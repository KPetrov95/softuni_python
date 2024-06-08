CREATE OR REPLACE FUNCTION fn_full_name(first_name varchar(50), last_name varchar(50))
RETURNS VARCHAR(101) AS
$$
    BEGIN
        RETURN CONCAT(INITCAP(first_name), ' ', INITCAP(last_name));
    end;
$$
LANGUAGE plpgsql