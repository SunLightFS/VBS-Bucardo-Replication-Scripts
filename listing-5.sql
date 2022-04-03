create or replace function check_data()
returns trigger
AS $function$
    declare
        new_session_id varchar;
    begin
        if (TG_OP = 'INSERT' and NEW.leg_id in
		            (select leg_id from call_legs where session_id = NEW.session_id)) then
            new_session_id = (select new_session_id from id_transfer where old_session_id = NEW.session_id);
            if (new_session_id is null) then
                loop
                    exit when new_session_id not in (select session_id from call_legs);
                    new_session_id = new_session_id + 100;
                end loop;
                insert into id_transfer values (NEW.session_id, new_session_id);
            end if;
            NEW.session_id = new_session_id
            insert into call_legs values (NEW);
            return null;
        end if;
        return NEW;
    end;
    $function$
language plpgsql;
