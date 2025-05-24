CREATE TABLE departamento (
  dep_Id INTEGER PRIMARY KEY AUTO_INCREMENT,
  dep_name TEXT NOT NULL
);
-- insert
INSERT INTO departamento (dep_name) VALUES ('Vendas');
INSERT INTO departamento (dep_name) VALUES ('Contabilidade');
INSERT INTO departamento (dep_name) VALUES ('Gerencia');
INSERT INTO departamento (dep_name) VALUES ('Criador de Vulgo');
INSERT INTO departamento (dep_name) VALUES ('Domador de Pôneis');

INSERT INTO departamento (dep_name, dep_Id) VALUES ('Recursos Humanos', 15);

INSERT INTO departamento (dep_name) VALUES ('Relações Internacionais');

INSERT INTO departamento (dep_name) VALUES ('Estagiaria');

-- create
CREATE TABLE empregado (
    emp_Id INTEGER PRIMARY KEY AUTO_INCREMENT,
    emp_name TEXT NOT NULL,
    emp_dept integer, -- NOT NULL
    emp_sal DECIMAL
    
    -- FOREIGN KEY emp_dep_fk (emp_dept)
    --     REFERENCES departamento (dep_Id)
    --     ON DELETE restrict -- cascade
    -- );
);

 ALTER TABLE empregado ADD CONSTRAINT
    emp_dep_fk FOREIGN KEY (emp_dept) REFERENCES departamento (dep_Id)
    ON DELETE RESTRICT;

-- insert
INSERT INTO empregado (emp_name, emp_dept, emp_sal) VALUES ('Carlos', 4, 35800);
INSERT INTO empregado (emp_name, emp_dept, emp_sal) VALUES ('Kauê', 17, 100);
INSERT INTO empregado (emp_name, emp_dept, emp_sal) VALUES ('Gustavo', 5, 1249);
INSERT INTO empregado (emp_name, emp_dept, emp_sal) VALUES ('Milena', 15, 2000);
INSERT INTO empregado (emp_name, emp_dept, emp_sal) VALUES ('Ana', 15, 2001);
INSERT INTO empregado (emp_name, emp_dept, emp_sal) VALUES ('Wellington', 3, 9000000);
INSERT INTO empregado (emp_name, emp_dept, emp_sal) VALUES ('Karina', 17, 99.49);


-- select * from empregado;
-- select * from departamento;

SELECT count(emp_dept) qtd_dept FROM empregado;

-- UPDATE empregado SET emp_dept = NULL;
-- WHERE emp_Id = 4 or emp_Id = 2 or emp_Id = 7;

SELECT count(*) qtd_empregados FROM empregado;
SELECT count(emp_dept) qtd_dept FROM empregado;

select emp_name,
       emp_dept,
       emp_sal,
       dep_name
from empregado
    join departamento on departamento.dep_Id = empregado.emp_dept
    -- and departamento.dep_Id = 1
    order by 3,1;

SELECT emp_dept, sum(emp_sal) soma FROM empregado GROUP BY  emp_dept;

-- select * from departamento;


-- fetch 
-- SELECT emp_name FROM empregado  WHERE emp_name like 'A%';
-- SELECT * FROM empregado;
