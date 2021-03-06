% FORMAT C = set_icecube(P,C) 
%
% OUT   C      Extended, with C.pol_mode set
% IN    P      Path structure
%       C      Calculation settings structure
%
% Sets
%    f_grid
%    stokes_dim
%    absorption.arts

% 2021-01-11 Patrick Eriksson

function C = set_cloudsat(P,C)


%- Output
%
C.pol_mode = 'H';  % To get increased backscattering for polratio > 1


%- f_grid
%
xmlStore( fullfile( P.wfolder, 'f_grid.xml' ), 94e9, 'Vector' );


%- stokes
%
xmlStore( fullfile( P.wfolder, 'stokes_dim.xml' ), 1, 'Index' );


%- Species and absorption files
%
copyfile( fullfile( P.arts_files, 'continua_rttov.arts' ), ...
          fullfile( P.wfolder, 'continua.arts' ) );
copyfile( fullfile( P.arts_files, 'abs_lines_h2o_rttov_below340ghz.xml' ), ...
          fullfile( P.wfolder, 'abs_lines_h2o_rttov_below340ghz.xml' ) );
copyfile( fullfile(P.arts_files,'absorption_gmi.arts'), ...
          fullfile(P.wfolder,'absorption.arts') );
