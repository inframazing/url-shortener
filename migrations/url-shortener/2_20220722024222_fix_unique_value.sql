-- upgrade --
CREATE UNIQUE INDEX "uid_TA_Urls_url_sho_99780a" ON "TA_Urls" ("url_shorten");
-- downgrade --
DROP INDEX "idx_TA_Urls_url_sho_99780a";
