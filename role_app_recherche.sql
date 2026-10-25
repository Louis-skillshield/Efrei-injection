-- ============================================================
-- Journée 4 · Sécurité · S6 (bonus) : un rôle dédié à l'appli
-- Base : velib_db — à exécuter en tant que propriétaire de la base :
--   psql -U {username} -d velib_db -f role_app_recherche.sql
--
-- Les rôles PostgreSQL sont communs à TOUTES les bases du serveur :
-- on les crée une fois, on donne ensuite des droits base par base.
-- ============================================================


-- ------------------------------------------------------------
-- 0. Repartir de zéro (permet de rejouer le script)
-- ------------------------------------------------------------
DROP OWNED BY app_recherche;     -- retire tous les droits donnés à app_recherche dans cette base
DROP ROLE IF EXISTS app_recherche;
-- (au tout premier lancement, DROP OWNED affiche une erreur
--  « role does not exist » : c'est normal, on peut l'ignorer)


-- ------------------------------------------------------------
-- 1. Un rôle pour l'appli de recherche d'abonnés
--    Moindre privilège : elle ne fait QUE lire la table abonne.
-- ------------------------------------------------------------
CREATE ROLE app_recherche LOGIN PASSWORD 'app_recherche_j4';

GRANT CONNECT ON DATABASE velib_db TO app_recherche;
GRANT USAGE ON SCHEMA public TO app_recherche;
GRANT SELECT ON abonne TO app_recherche;

-- Ensuite : dans .env, DB_USER=app_recherche et DB_PASSWORD=app_recherche_j4,
-- puis relancer l'appli et rejouer l'attaque UNION en version vulnérable.
