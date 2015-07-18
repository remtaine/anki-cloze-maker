# anki-cloze-maker
specific version of anki-note-maker, focusing on cloze and lists

example input:
    
    The capital of @Zimbabwe is @Harrare

output:
    
    The capital of {{c1::Zimbabwe}} is {{c2::Harrare}} 

example input:

    ###Colors of the Rainbow
    ##red
    ##orange
    ##yellow
    ##green
    ##blue
    ##indigo
    ##violet
    ###

output:

    Colors of the rainbow: 1){{c1::red}} 2)orange
    Colors of the rainbow: 1)red}} 2){{c2::orange}} 3)yellow 
    Colors of the rainbow: 2)orange 3){{c3::yellow}} 4)green 
    Colors of the rainbow: 3)yellow 4){{c4::green}} 5)blue
    Colors of the rainbow: 4)green 5){{c5::blue}} 6)indigo 
    Colors of the rainbow: 5)blue 6){{c6::indigo}} 7)violet
    Colors of the rainbow: 6)indigo 7){{c7::violet}}

