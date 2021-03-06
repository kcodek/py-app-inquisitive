/*
 * SQLite SELECT TABLE examples.
 * 
 */

--
-- master
--
-- SELECT * FROM master ORDER BY RANDOM() LIMIT 3;
-- select german_word,frequency,difficulty from master where german_word='weder … noch';
-- select german_word,frequency,difficulty from master where frequency>0 ;
select german_word,frequency,difficulty from master where difficulty<0;
select german_word,frequency,difficulty from master where difficulty<0 AND (partsofspeech='verb');
select german_word,frequency,difficulty from master where difficulty>0 AND (partsofspeech='verb');

select german_word,frequency,difficulty from master where difficulty>0 AND (partsofspeech='sentence');
select german_word,frequency,difficulty from master where difficulty<0 AND (partsofspeech='sentence');
-- select german_word,frequency,difficulty from master where difficulty>0 AND (partsofspeech='verb' OR partsofspeech='conjunction');

--
-- conjunction
--
SELECT * FROM conjunction ORDER BY RANDOM() LIMIT 3;

--
-- verb
--
SELECT * FROM verb ORDER BY RANDOM() LIMIT 3;


--
-- noun
--
SELECT * FROM noun ORDER BY RANDOM() LIMIT 3;




--
-- sentence
--
SELECT * FROM sentence ORDER BY RANDOM() LIMIT 3;