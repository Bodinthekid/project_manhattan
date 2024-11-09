CREATE TABLE la_liga_teams (
    team_id VARCHAR(20)  ID PRIMARY KEY NOT NULL,   -- Identificador único para cada time
    idAPIfootball VARCHAR(10) NULL,          -- Nome do time
    strTeam VARCHAR(80) NOT NULL,                         -- Ano de fundação do time
    strTeamShort VARCHAR(80) NULL,                    -- Nome do estádio
    strTeamShort VARCHAR(7) NULL,                        -- Cidade onde o time está localizado
    intFormedYear VARCHAR(4) NULL,                       -- Nome do treinador
    strSport VARCHAR(10) NULL
    strLocation VARCHAR(3O) NULL
    strStadium VARCHAR(3O) NULL
    strDescriptionEN VARCHAR(250) NULL
    strGender VARCHAR(10) NULL
    strCountry VARCHAR(10) NULL
    strBadge VARCHAR(250) NULL
    strLogo VARCHAR(250) NULL
);
