-- Resetar o banco para garantir que o teste seja limpo
DROP DATABASE IF EXISTS oxetech;
CREATE DATABASE oxetech;
USE oxetech;

-- 1. Tabela Forte: CURSOS 
CREATE TABLE cursos (
    id_curso INT AUTO_INCREMENT PRIMARY KEY,
    nome_curso VARCHAR(50) NOT NULL,
    carga_horaria INT,
    coordenador VARCHAR(50) DEFAULT 'Coordenadora'
);

-- 2. Tabela Forte: ALUNOS (Cadastro das pessoas)
CREATE TABLE alunos (
    id_aluno INT AUTO_INCREMENT PRIMARY KEY,
    nome_aluno VARCHAR(60) NOT NULL,
    email VARCHAR(60) UNIQUE
);

-- 3. Tabela Associativa: MATRICULAS (Onde a 'mágica' das Chaves Estrangeiras acontece)
CREATE TABLE matriculas (
    id_matricula INT AUTO_INCREMENT PRIMARY KEY,
    data_matricula DATE,
    -- Criando as colunas que receberão os IDs
    id_aluno INT,
    id_curso INT,
    -- Definindo as regras de Chave Estrangeira (FK)
    CONSTRAINT fk_aluno_matricula FOREIGN KEY (id_aluno) 
        REFERENCES alunos(id_aluno),
    CONSTRAINT fk_curso_matricula FOREIGN KEY (id_curso) 
        REFERENCES cursos(id_curso)
);

-- Resetar o banco para garantir que o teste seja limpo
DROP DATABASE IF EXISTS oxetech;
CREATE DATABASE oxetech;
USE oxetech;

-- 1. Tabela Forte: CURSOS 
CREATE TABLE cursos (
    id_curso INT AUTO_INCREMENT PRIMARY KEY,
    nome_curso VARCHAR(50) NOT NULL,
    carga_horaria INT,
    coordenador VARCHAR(50) DEFAULT 'Coordenadora'
);

-- 2. Tabela Forte: ALUNOS (Cadastro das pessoas)
CREATE TABLE alunos (
    id_aluno INT AUTO_INCREMENT PRIMARY KEY,
    nome_aluno VARCHAR(60) NOT NULL,
    email VARCHAR(60) UNIQUE
);

-- 3. Tabela Associativa: MATRICULAS (Onde a mágica das Chaves Estrangeiras acontece)
CREATE TABLE matriculas (
    id_matricula INT AUTO_INCREMENT PRIMARY KEY,
    data_matricula DATE,
    -- Criando as colunas que receberão os IDs
    id_aluno INT,
    id_curso INT,
    -- Definindo as regras de Chave Estrangeira (FK)
    CONSTRAINT fk_aluno_matricula FOREIGN KEY (id_aluno) 
        REFERENCES alunos(id_aluno),
    CONSTRAINT fk_curso_matricula FOREIGN KEY (id_curso) 
        REFERENCES cursos(id_curso)
);

-- Inserindo os cursos da Oxetech
INSERT INTO cursos (nome_curso, carga_horaria) VALUES 
('Lógica de Programação', 40),
('Banco de Dados', 60),
('Análise de Dados', 50);

-- Inserindo Alunos
INSERT INTO alunos (nome_aluno, email) VALUES 
('João Silva', 'joao@email.com'),
('Maria Oliveira', 'maria@email.com'),
('Pedro Santos', 'pedro@email.com'),
('Ana Souza', 'ana@email.com'),
('Lucas Pereira', 'lucas@email.com');

-- Inserindo as Matrículas (Relacionando IDs de Alunos com IDs de Cursos)
-- Vamos supor que:
-- Curso 1 = Lógica | Curso 2 = Banco | Curso 3 = Análise

INSERT INTO matriculas (id_aluno, id_curso, data_matricula) VALUES 
(1, 1, '2023-10-01'), -- João faz Lógica
(1, 2, '2023-10-05'), -- João TAMBÉM faz Banco de Dados
(2, 1, '2023-10-01'), -- Maria faz Lógica
(3, 3, '2023-10-02'), -- Pedro faz Análise de Dados
(4, 2, '2023-10-10'), -- Ana faz Banco de Dados
(5, 1, '2023-10-12'), -- Lucas faz Lógica
(5, 2, '2023-10-12'), -- Lucas faz Banco de Dados
(5, 3, '2023-10-15'); -- Lucas estuda muito (faz os três!)

SELECT 
    m.id_matricula,
    a.nome_aluno,
    c.nome_curso,
    c.coordenador
FROM matriculas m
JOIN alunos a ON m.id_aluno = a.id_aluno
JOIN cursos c ON m.id_curso = c.id_curso
ORDER BY a.nome_aluno;
