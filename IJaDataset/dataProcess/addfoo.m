indir ="D:\proData\826\bcb_new\";
outdir="D:\proData\826\bcb_foo\";

File = dir(fullfile(indir,'*.txt'));
FileNames = {File.name}'; 
Length_Names = size(FileNames,1); 
for k = 1 : Length_Names
    % FileNames(k)
    fidin=fopen(indir+FileNames{k},'r');
    if fidin==-1
        return;
    end
    fidout=fopen(outdir+FileNames{k},'w');
    fprintf(fidout,'%s\n',"public class DUMMY_CLASS_FOO {");
    while ~feof(fidin) % 判断是否为文件末尾  
        tline=fgetl(fidin); % 从文件读行
        fprintf(fidout,'%s\n',tline);
    end
    fprintf(fidout,'%s\n',"}");
    fclose(fidin);
    fclose(fidout);
end
