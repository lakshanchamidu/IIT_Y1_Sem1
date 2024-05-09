from graphics import *   #import the graphics.py module (must be in the same folder this file)

def Graph(Graph_list):
#OPEN THE WINDOW
    win = GraphWin("Histogram", 800, 600)
    win.setBackground("Mint Cream")

    max_count = 40
    Scale = 1200/max_count
    Progress_height_count = Graph_list.count("Progress")
    Trailer_height_count = Graph_list.count("Progress (module trailer)")
    Retriever_height_count = Graph_list.count("Module retriever")
    Exclude_height_count = Graph_list.count("Exclude")
    total_outcomes = Progress_height_count + Trailer_height_count + Retriever_height_count + Exclude_height_count
    
    heading = Text(Point(330,20),'Histrogram Result')
    heading.setSize(14)
    heading.draw(win)

    Progress_bar = Rectangle(Point(100,500), Point(210,500 - (Scale * Progress_height_count)))
    Progress_bar.setFill("Yellow")
    Progress_bar.setWidth(1)
    Progress_bar.draw(win)
    Progress = Text(Point(153,513),'Progress')
    Progress.setSize(15)
    Progress.draw(win)
    Progress_outcomes = Text(Point(153,540),Progress_height_count)
    Progress_outcomes.setSize(15)
    Progress_outcomes.draw(win)

    Trailer_bar = Rectangle(Point(218,500), Point(328,500 - (Scale * Trailer_height_count)))
    Trailer_bar.setFill("Purple")
    Trailer_bar.setWidth(1)
    Trailer_bar.draw(win)
    Trailer = Text(Point(274,513),'Trailer')
    Trailer.setSize(15)
    Trailer.draw(win)
    Trailer_outcomes = Text(Point(274,540),Trailer_height_count)
    Trailer_outcomes.setSize(15)
    Trailer_outcomes.draw(win)

    Retriever_bar = Rectangle(Point(336,500), Point(446,500 - (Scale * Retriever_height_count)))
    Retriever_bar.setFill("Red")
    Retriever_bar.setWidth(1)
    Retriever_bar.draw(win)
    Retriever = Text(Point(390,513),'Retriever')
    Retriever.setSize(15)
    Retriever.draw(win)
    Retriever_outcomes = Text(Point(390,540 ),Retriever_height_count)
    Retriever_outcomes.setSize(15)
    Retriever_outcomes.draw(win)

    Exclude_bar = Rectangle(Point(454,500), Point(564,500 - (Scale * Exclude_height_count)))
    Exclude_bar.setFill("Blue")
    Exclude_bar.setWidth(1)
    Exclude_bar.draw(win)
    Exclude = Text(Point(510,513),'Exclude')
    Exclude.setSize(15)
    Exclude.draw(win)
    Exclude_outcomes = Text(Point(504,540),Exclude_height_count)
    Exclude_outcomes.setSize(15)
    Exclude_outcomes.draw(win)

    line = Line(Point(50,500), Point(614,500))
    line.setWidth(2)
    line.draw(win)

    total = Text(Point(150,560),str(total_outcomes) + " Outcomes in Total")
    total.setSize(15)
    total.draw(win)


