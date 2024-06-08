CREATE OR REPLACE FUNCTION fn_calculate_future_value(initial_sum numeric, yearly_interest_rate numeric, number_of_years int)
RETURNS NUMERIC AS
$$
    DECLARE
        future_value numeric;
    BEGIN
        future_value = TRUNC(initial_sum * power(1 + yearly_interest_rate, number_of_years), 4);
        RETURN future_value;
    end;
$$
LANGUAGE plpgsql