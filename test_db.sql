--
-- PostgreSQL database dump
--

-- Dumped from database version 10.12 (Ubuntu 10.12-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.12 (Ubuntu 10.12-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: event_type; Type: TABLE; Schema: public; Owner: wilfred
--

CREATE TABLE public.event_type (
    id integer NOT NULL,
    name character varying,
    description character varying,
    create_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.event_type OWNER TO wilfred;

--
-- Name: event_type_id_seq; Type: SEQUENCE; Schema: public; Owner: wilfred
--

CREATE SEQUENCE public.event_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.event_type_id_seq OWNER TO wilfred;

--
-- Name: event_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wilfred
--

ALTER SEQUENCE public.event_type_id_seq OWNED BY public.event_type.id;


--
-- Name: events; Type: TABLE; Schema: public; Owner: wilfred
--

CREATE TABLE public.events (
    id integer NOT NULL,
    title character varying,
    description character varying,
    start_date_time timestamp without time zone,
    address character varying,
    image character varying,
    price double precision,
    event_type_id integer
);


ALTER TABLE public.events OWNER TO wilfred;

--
-- Name: events_id_seq; Type: SEQUENCE; Schema: public; Owner: wilfred
--

CREATE SEQUENCE public.events_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.events_id_seq OWNER TO wilfred;

--
-- Name: events_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wilfred
--

ALTER SEQUENCE public.events_id_seq OWNED BY public.events.id;


--
-- Name: tickets; Type: TABLE; Schema: public; Owner: wilfred
--

CREATE TABLE public.tickets (
    id integer NOT NULL,
    event_id integer,
    attender_email character varying,
    create_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.tickets OWNER TO wilfred;

--
-- Name: tickets_id_seq; Type: SEQUENCE; Schema: public; Owner: wilfred
--

CREATE SEQUENCE public.tickets_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tickets_id_seq OWNER TO wilfred;

--
-- Name: tickets_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wilfred
--

ALTER SEQUENCE public.tickets_id_seq OWNED BY public.tickets.id;


--
-- Name: event_type id; Type: DEFAULT; Schema: public; Owner: wilfred
--

ALTER TABLE ONLY public.event_type ALTER COLUMN id SET DEFAULT nextval('public.event_type_id_seq'::regclass);


--
-- Name: events id; Type: DEFAULT; Schema: public; Owner: wilfred
--

ALTER TABLE ONLY public.events ALTER COLUMN id SET DEFAULT nextval('public.events_id_seq'::regclass);


--
-- Name: tickets id; Type: DEFAULT; Schema: public; Owner: wilfred
--

ALTER TABLE ONLY public.tickets ALTER COLUMN id SET DEFAULT nextval('public.tickets_id_seq'::regclass);


--
-- Data for Name: event_type; Type: TABLE DATA; Schema: public; Owner: wilfred
--

INSERT INTO public.event_type VALUES (1, 'Python Tech', 'Event for python developers all over the world', '2020-04-03 09:08:09.241025', '2020-04-03 09:08:09.241164');
INSERT INTO public.event_type VALUES (2, 'Python Tech', 'Event for python developers all over the world', '2020-04-03 09:10:34.32706', '2020-04-03 09:10:34.32717');
INSERT INTO public.event_type VALUES (3, 'Python Tech', 'Event for python developers all over the world', '2020-04-03 09:17:43.301957', '2020-04-03 09:17:43.302066');
INSERT INTO public.event_type VALUES (4, 'Python Tech', 'Event for python developers all over the world', '2020-04-03 09:17:50.127644', '2020-04-03 09:17:50.127753');
INSERT INTO public.event_type VALUES (5, 'Python Tech', 'Event for python developers all over the world', '2020-04-03 09:17:52.76687', '2020-04-03 09:17:52.766981');
INSERT INTO public.event_type VALUES (6, 'Python Tech', 'Event for python developers all over the world', '2020-04-03 09:17:55.673783', '2020-04-03 09:17:55.673892');
INSERT INTO public.event_type VALUES (7, 'Python Tech', 'Event for python developers all over the world', '2020-04-03 09:17:58.885213', '2020-04-03 09:17:58.88533');
INSERT INTO public.event_type VALUES (8, 'Python Tech', 'Event for python developers all over the world', '2020-04-03 09:18:01.386113', '2020-04-03 09:18:01.386221');
INSERT INTO public.event_type VALUES (9, 'Python Tech', 'Event for python developers all over the world', '2020-04-03 09:18:04.002375', '2020-04-03 09:18:04.002485');
INSERT INTO public.event_type VALUES (10, 'Python Tech', 'Event for python developers all over the world', '2020-04-03 09:18:07.140018', '2020-04-03 09:18:07.140129');
INSERT INTO public.event_type VALUES (11, 'Python Tech', 'Event for python developers all over the world', '2020-04-03 09:18:09.686572', '2020-04-03 09:18:09.686684');
INSERT INTO public.event_type VALUES (12, 'Python Tech', 'Event for python developers all over the world', '2020-04-03 09:18:12.923765', '2020-04-03 09:18:12.923881');
INSERT INTO public.event_type VALUES (13, 'Python Tech', 'Event for python developers all over the world', '2020-04-03 09:18:15.841339', '2020-04-03 09:18:15.84145');
INSERT INTO public.event_type VALUES (14, 'Python Tech', 'Event for python developers all over the world', '2020-04-03 09:18:22.612569', '2020-04-03 09:18:22.612682');
INSERT INTO public.event_type VALUES (15, 'Python Tech', 'Event for python developers all over the world', '2020-04-03 09:18:30.296949', '2020-04-03 09:18:30.29706');
INSERT INTO public.event_type VALUES (16, 'Python Tech', 'Event for python developers all over the world', '2020-04-03 09:50:58.273766', '2020-04-03 09:50:58.273878');


--
-- Data for Name: events; Type: TABLE DATA; Schema: public; Owner: wilfred
--

INSERT INTO public.events VALUES (2, 'Markup Start', 'This is an event I am creating for meeting with ', '2020-05-30 15:45:00', 'Douala Bonamoussadi', NULL, 2000, 1);
INSERT INTO public.events VALUES (3, 'Markup Start', 'This is an event I am creating for meeting with ', '2020-05-30 15:45:00', 'Douala Bonamoussadi', NULL, 2000, 1);
INSERT INTO public.events VALUES (4, 'Markup Start', 'This is an event I am creating for meeting with ', '2020-05-30 15:45:00', 'Douala Bonamoussadi', NULL, 2000, 1);
INSERT INTO public.events VALUES (5, 'Markup Start', 'This is an event I am creating for meeting with ', '2020-05-30 15:45:00', 'Douala Bonamoussadi', NULL, 2000, 1);
INSERT INTO public.events VALUES (6, 'Markup Start', 'This is an event I am creating for meeting with ', '2020-05-30 15:45:00', 'Douala Bonamoussadi', NULL, 2000, 1);
INSERT INTO public.events VALUES (7, 'Markup Start', 'This is an event I am creating for meeting with ', '2020-05-30 15:45:00', 'Douala Bonamoussadi', NULL, 2000, 1);
INSERT INTO public.events VALUES (8, 'Markup Start', 'This is an event I am creating for meeting with ', '2020-05-30 15:45:00', 'Douala Bonamoussadi', NULL, 2000, 1);
INSERT INTO public.events VALUES (9, 'Markup Start', 'This is an event I am creating for meeting with ', '2020-05-30 15:45:00', 'Douala Bonamoussadi', NULL, 2000, 1);
INSERT INTO public.events VALUES (10, 'Markup Start', 'This is an event I am creating for meeting with ', '2020-05-30 15:45:00', 'Douala Bonamoussadi', NULL, 2000, 1);
INSERT INTO public.events VALUES (11, 'Markup Start', 'This is an event I am creating for meeting with ', '2020-05-30 15:45:00', 'Douala Bonamoussadi', NULL, 2000, 1);
INSERT INTO public.events VALUES (12, 'Markup Start', 'This is an event I am creating for meeting with ', '2020-05-30 15:45:00', 'Douala Bonamoussadi', NULL, 2000, 1);
INSERT INTO public.events VALUES (13, 'Markup Start', 'This is an event I am creating for meeting with ', '2020-05-30 15:45:00', 'Douala Bonamoussadi', NULL, 2000, 1);
INSERT INTO public.events VALUES (14, 'Markup Start', 'This is an event I am creating for meeting with ', '2020-05-30 15:45:00', 'Douala Bonamoussadi', NULL, 2000, 1);
INSERT INTO public.events VALUES (15, 'Markup Start', 'This is an event I am creating for meeting with ', '2020-05-30 15:45:00', 'Douala Bonamoussadi', NULL, 2000, 1);
INSERT INTO public.events VALUES (16, 'Markup Start', 'This is an event I am creating for meeting with ', '2020-05-30 15:45:00', 'Douala Bonamoussadi', NULL, 2000, 1);
INSERT INTO public.events VALUES (1, 'Markup Start', 'This is an event I am creating for meeting with ', '2020-05-30 15:45:00', 'Douala Bonamoussadi', NULL, 2000, 1);


--
-- Data for Name: tickets; Type: TABLE DATA; Schema: public; Owner: wilfred
--

INSERT INTO public.tickets VALUES (1, 1, 'chetat@gmail.com', '2020-04-03 09:08:09.246058', '2020-04-03 09:08:09.246085');
INSERT INTO public.tickets VALUES (2, 1, 'chetat@gmail.com', '2020-04-03 09:10:34.332013', '2020-04-03 09:10:34.332041');
INSERT INTO public.tickets VALUES (3, 1, 'chetat@gmail.com', '2020-04-03 09:17:43.306881', '2020-04-03 09:17:43.306909');
INSERT INTO public.tickets VALUES (4, 1, 'chetat@gmail.com', '2020-04-03 09:17:50.132565', '2020-04-03 09:17:50.132593');
INSERT INTO public.tickets VALUES (5, 1, 'chetat@gmail.com', '2020-04-03 09:17:52.771853', '2020-04-03 09:17:52.77188');
INSERT INTO public.tickets VALUES (6, 1, 'chetat@gmail.com', '2020-04-03 09:17:55.678842', '2020-04-03 09:17:55.678871');
INSERT INTO public.tickets VALUES (7, 1, 'chetat@gmail.com', '2020-04-03 09:17:58.89029', '2020-04-03 09:17:58.890317');
INSERT INTO public.tickets VALUES (8, 1, 'chetat@gmail.com', '2020-04-03 09:18:01.391047', '2020-04-03 09:18:01.391074');
INSERT INTO public.tickets VALUES (9, 1, 'chetat@gmail.com', '2020-04-03 09:18:04.007354', '2020-04-03 09:18:04.007381');
INSERT INTO public.tickets VALUES (10, 1, 'chetat@gmail.com', '2020-04-03 09:18:07.145035', '2020-04-03 09:18:07.145062');
INSERT INTO public.tickets VALUES (11, 1, 'chetat@gmail.com', '2020-04-03 09:18:09.695114', '2020-04-03 09:18:09.695166');
INSERT INTO public.tickets VALUES (12, 1, 'chetat@gmail.com', '2020-04-03 09:18:12.928906', '2020-04-03 09:18:12.928935');
INSERT INTO public.tickets VALUES (13, 1, 'chetat@gmail.com', '2020-04-03 09:18:15.846267', '2020-04-03 09:18:15.846294');
INSERT INTO public.tickets VALUES (14, 1, 'chetat@gmail.com', '2020-04-03 09:18:22.617685', '2020-04-03 09:18:22.617711');
INSERT INTO public.tickets VALUES (15, 1, 'chetat@gmail.com', '2020-04-03 09:18:30.301927', '2020-04-03 09:18:30.301953');
INSERT INTO public.tickets VALUES (16, 1, 'chetat@gmail.com', '2020-04-03 09:50:58.278826', '2020-04-03 09:50:58.278853');


--
-- Name: event_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wilfred
--

SELECT pg_catalog.setval('public.event_type_id_seq', 16, true);


--
-- Name: events_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wilfred
--

SELECT pg_catalog.setval('public.events_id_seq', 16, true);


--
-- Name: tickets_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wilfred
--

SELECT pg_catalog.setval('public.tickets_id_seq', 16, true);


--
-- Name: event_type event_type_pkey; Type: CONSTRAINT; Schema: public; Owner: wilfred
--

ALTER TABLE ONLY public.event_type
    ADD CONSTRAINT event_type_pkey PRIMARY KEY (id);


--
-- Name: events events_pkey; Type: CONSTRAINT; Schema: public; Owner: wilfred
--

ALTER TABLE ONLY public.events
    ADD CONSTRAINT events_pkey PRIMARY KEY (id);


--
-- Name: tickets tickets_pkey; Type: CONSTRAINT; Schema: public; Owner: wilfred
--

ALTER TABLE ONLY public.tickets
    ADD CONSTRAINT tickets_pkey PRIMARY KEY (id);


--
-- Name: ix_event_type_create_at; Type: INDEX; Schema: public; Owner: wilfred
--

CREATE INDEX ix_event_type_create_at ON public.event_type USING btree (create_at);


--
-- Name: ix_event_type_updated_at; Type: INDEX; Schema: public; Owner: wilfred
--

CREATE INDEX ix_event_type_updated_at ON public.event_type USING btree (updated_at);


--
-- Name: ix_events_start_date_time; Type: INDEX; Schema: public; Owner: wilfred
--

CREATE INDEX ix_events_start_date_time ON public.events USING btree (start_date_time);


--
-- Name: ix_tickets_create_at; Type: INDEX; Schema: public; Owner: wilfred
--

CREATE INDEX ix_tickets_create_at ON public.tickets USING btree (create_at);


--
-- Name: ix_tickets_id; Type: INDEX; Schema: public; Owner: wilfred
--

CREATE INDEX ix_tickets_id ON public.tickets USING btree (id);


--
-- Name: ix_tickets_updated_at; Type: INDEX; Schema: public; Owner: wilfred
--

CREATE INDEX ix_tickets_updated_at ON public.tickets USING btree (updated_at);


--
-- PostgreSQL database dump complete
--

