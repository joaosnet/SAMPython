-- Module: testbench for Multiplication by Successive Additions - SAM
-- Autor: João da Cruz de Nativiade e Silva Neto
-- Date: Sun Aug 25 22:08:23 2024

-- Curso: Engenharia de Computação
-- Disciplina: Projetos de Hardware e Interfaceamento

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use std.textio.all;

entity testbench is
end testbench;

architecture test of testbench is
    component sd
        port(
            Reset: in std_logic;
            ck: in std_logic;
            entA: in unsigned(3 downto 0);
            entB: in unsigned(3 downto 0);
            mult: out unsigned(3 downto 0);
            pronto: out std_logic
        );
    end component;

    signal Reset: std_logic := '0';
    signal ck: std_logic := '0';
    signal entA, entB: unsigned(3 downto 0);
    signal mult: unsigned(3 downto 0);
    signal pronto: std_logic;
    signal counter: integer := 0;

begin
    dut: sd
    port map(
        Reset => Reset,
        ck => ck,
        entA => entA,
        entB => entB,
        mult => mult,
        pronto => pronto
    );

    process(ck)
        file F: TEXT open READ_MODE is "c:\users\joaod\documents\2024.2\phi\entradas.txt";
        variable L: LINE;
        variable entrada : integer;
    begin
        if rising_edge(ck) then
            if counter = 0 then
                Reset <= '1';
            elsif counter = 1 then
                Reset <= '0';
            end if;

            if pronto = '1' then
                if not endfile(F) then
                    READLINE(F, L);
                    READ(L, entrada);
                    entA <= unsigned(to_unsigned(entrada, 4));

                    READLINE(F, L);
                    READ (L, entrada);
                    entB <= unsigned(to_unsigned(entrada, 4));
                end if;
            else
                counter <= counter + 1;
            end if;
            
            if counter = 2 then
                if not endfile(F) then
                    READLINE(F, L);
                    READ(L, entrada);
                    entA <= unsigned(to_unsigned(entrada, 4));

                    READLINE(F, L);
                    READ (L, entrada);
                    entB <= unsigned(to_unsigned(entrada, 4));
                end if;
            end if;
        end if;
    end process; 

    process(ck)
        file F: TEXT open WRITE_MODE is "c:\users\joaod\documents\2024.2\phi\saida.txt";
        variable L: LINE;
    begin
        if rising_edge(ck) then

            if Reset = '1' then
                WRITE(L, STRING'("entA entB mult"));
                WRITELINE(F, L);
                WRITE(L, STRING'("----------------"));
                WRITELINE(F, L);
            end if;

            if pronto = '1' then
                WRITE(L, ' ');
                WRITE(L, to_integer(entA));
                WRITE(L, ' ');
                WRITE(L, to_integer(entB));
                WRITE(L, ' ');
                WRITE(L, to_integer(mult));
                WRITELINE(F, L);
            end if;
        end if;
    end process;

    ck <= not ck after 5 ns;

end test;