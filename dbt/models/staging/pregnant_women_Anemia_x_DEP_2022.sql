{{ config(materialized="table") }}

select *,
    CAST('2022-06-01' as date) as Date_range,
    'pregnant women' as Category, 
    from {{ source("staging", "pregnant_women_Anemia x DEP_2022_01_06") }}
UNION ALL 
select *,
    CAST('2022-09-01' as date) as Date_range,
    'pregnant women' as Category, 
    from {{ source("staging", "pregnant_women_Anemia x DEP_2022_01_09") }}
