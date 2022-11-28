-- Join query
select e.date,e.cur_location_id from E_Accessory as e inner join Accessory_type as a on e.accessory_id=a.type_id where a.type_desc="Apple";

-- Trigger
DELIMITER $$  
      
    CREATE TRIGGER backup_office
    BEFORE DELETE  
    ON office FOR EACH ROW  
    BEGIN  
        INSERT INTO backup_office SELECT*FROM office WHERE office.office_id=OLD.office_id;
    END$$   
      
    DELIMITER ;


-- Set Operation

SELECT * FROM E_Accessory
WHERE E_Accessory.Brand="Apple"
UNION
SELECT E_Accessory.accessory_id, E_Accessory.model, E_Accessory.brand, E_Accessory.cur_location_id, E_Accessory.date
FROM E_Accessory
JOIN office
ON office.office_id=E_Accessory.cur_location_id;