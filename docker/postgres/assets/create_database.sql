CREATE DATABASE "cilada"
  WITH OWNER = postgres
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'en_US.utf8'
	   LC_CTYPE = 'en_US.utf8'
       CONNECTION LIMIT = -1;

\connect cilada

GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;
COMMENT ON SCHEMA public IS 'standard public schema';
