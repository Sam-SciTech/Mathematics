from manim import *
import math

TEXT_COLOR = WHITE
ACCENT_COLOR = TEAL
HIGHLIGHT_COLOR = YELLOW
VECTOR_COLOR = BLUE
AXIS_COLOR = LIGHT_GREY
MATH_FONT_SIZE = 48
TEXT_FONT_SIZE = 40


class LinearAlgebraTitle(Scene):

    def construct(self):
        
        grid = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-6, 6, 1],
            background_line_style={"stroke_color": TEAL, "stroke_opacity": 0.2}
        )
        self.add(grid)

        
        title = Tex(r"Linear Algebra", font_size=80, color=TEXT_COLOR)
        subtitle = Tex(r"Part 1: Vectors, Intuition, and Operations", font_size=40, color=ACCENT_COLOR)

        title.to_edge(UP, buff=1.5)
        subtitle.next_to(title, DOWN)

        
        v1 = Arrow(start=ORIGIN, end=[2, 2, 0], color=YELLOW, buff=0)
        v2 = Arrow(start=ORIGIN, end=[-2, 1, 0], color=RED, buff=0)
        v3 = Arrow(start=ORIGIN, end=[1, -2, 0], color=BLUE, buff=0)

        vectors = VGroup(v1, v2, v3)

        
        self.play(DrawBorderThenFill(title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP))
        self.wait(1)

        self.play(LaggedStart(*[GrowArrow(v) for v in vectors], lag_ratio=0.2))
        self.wait(2)

        
        self.play(FadeOut(Group(title, subtitle, vectors, grid)))
        self.wait(1)


class TheShoppingProblem(Scene):
    """
    Scene 2: The 'Apple and Banana' Problem
    Reimagined with Cyber-Market Aesthetics and Laser Scanning.
    """

    def construct(self):
        
        
        
        
        self.camera.background_color = "

        HIGHLIGHT_COLOR = "
        TEAL_ACCENT = "
        RED_ACCENT = "

        
        def get_apple():
            body = Circle(radius=0.3, color="
            body.stretch(1.1, 0)
            stem = Line(body.get_top() + DOWN * 0.05, body.get_top() + UP * 0.15, color="
            leaf = Ellipse(width=0.2, height=0.1, color="
            leaf.move_to(stem.get_top()).shift(RIGHT * 0.1 + DOWN * 0.05).rotate(30 * DEGREES)
            shine = Arc(radius=0.2, start_angle=100 * DEGREES, angle=40 * DEGREES, color=WHITE, stroke_width=2,
                        stroke_opacity=0.4)
            shine.move_to(body.get_top() + LEFT * 0.1 + DOWN * 0.1)
            return VGroup(body, stem, leaf, shine)

        
        def get_banana():
            body = ArcBetweenPoints(LEFT * 0.35, RIGHT * 0.35, angle=-PI / 2.5, color="
            detail = ArcBetweenPoints(LEFT * 0.35, RIGHT * 0.35, angle=-PI / 2.5, color="
                                      stroke_width=3).shift(DOWN * 0.02)
            tip1 = Line(LEFT * 0.35, LEFT * 0.4, color="
            tip2 = Line(RIGHT * 0.35, RIGHT * 0.4, color="
            return VGroup(body, detail, tip1, tip2)

        
        def get_receipt(cost_text):
            paper = Rectangle(width=1.5, height=2, color="
            
            lines = VGroup(*[Line(LEFT * 0.5, RIGHT * 0.5, color="
            lines.arrange(DOWN, buff=0.3).move_to(paper).shift(UP * 0.3)

            
            cost = Tex(f"{cost_text}", color=BLACK, font_size=42).move_to(paper).shift(DOWN * 0.5)

            
            clip = RoundedRectangle(corner_radius=0.05, width=0.8, height=0.2, color="
                paper.get_top())

            return VGroup(paper, lines, cost, clip)

        
        X_LABEL = -6.0
        X_APPLE = -3.5
        X_PLUS = -1.5
        X_BANAN = 0.5
        X_RCPT = 4.0

        Y_TRIP1 = 2.0
        Y_TRIP2 = -1.0

        
        
        
        topic = Tex(r"\textbf{Why Linear Algebra?}", color=HIGHLIGHT_COLOR, font_size=60)
        topic_sub = Tex(r"From Fruit Markets to Data Science", color="

        self.play(Write(topic), FadeIn(topic_sub))
        self.wait(1.5)
        self.play(
            topic.animate.scale(0.6).to_edge(UP, buff=0.5),
            FadeOut(topic_sub)
        )

        
        
        

        
        trip1_label = Tex("Trip 1", font_size=36, color=TEAL_ACCENT).move_to(RIGHT * X_LABEL + UP * Y_TRIP1)

        apples_1 = VGroup(*[get_apple() for _ in range(2)]).arrange(RIGHT, buff=0.15).scale(0.7)
        apples_1.move_to(RIGHT * X_APPLE + UP * Y_TRIP1)

        plus_1 = MathTex("+").scale(1.2).move_to(RIGHT * X_PLUS + UP * Y_TRIP1)

        bananas_1 = VGroup(*[get_banana() for _ in range(3)]).arrange(RIGHT, buff=0.1).scale(0.7)
        bananas_1.move_to(RIGHT * X_BANAN + UP * Y_TRIP1)

        
        receipt_1 = get_receipt("8 Rs").scale(0.5).move_to(RIGHT * X_RCPT + UP * Y_TRIP1)

        
        shelf1 = Line(LEFT * 6, RIGHT * 6, color="

        self.play(Write(trip1_label), Create(shelf1))
        
        self.play(
            LaggedStart(
                ScaleInPlace(apples_1, 1.2, rate_func=wiggle),
                Write(plus_1),
                ScaleInPlace(bananas_1, 1.2, rate_func=wiggle),
                lag_ratio=0.2
            )
        )
        
        self.play(GrowFromEdge(receipt_1, UP), run_time=0.8)
        self.wait(0.5)

        
        trip2_label = Tex("Trip 2", font_size=36, color=TEAL_ACCENT).move_to(RIGHT * X_LABEL + UP * Y_TRIP2)

        apples_2_vis = VGroup(*[get_apple() for _ in range(3)]).arrange(RIGHT, buff=0.1)
        apples_2_txt = MathTex(r"\times 10", font_size=36).next_to(apples_2_vis, RIGHT, buff=0.2)
        apples_2 = VGroup(apples_2_vis, apples_2_txt).scale(0.7)
        apples_2.move_to(RIGHT * X_APPLE + UP * Y_TRIP2)

        plus_2 = MathTex("+").scale(1.2).move_to(RIGHT * X_PLUS + UP * Y_TRIP2)

        bananas_2 = VGroup(*[get_banana() for _ in range(1)]).arrange(RIGHT, buff=0.1).scale(0.7)
        bananas_2.move_to(RIGHT * X_BANAN + UP * Y_TRIP2)

        receipt_2 = get_receipt("13 Rs").scale(0.5).move_to(RIGHT * X_RCPT + UP * Y_TRIP2)

        shelf2 = Line(LEFT * 6, RIGHT * 6, color="

        self.play(Write(trip2_label), Create(shelf2))
        self.play(
            LaggedStart(
                ScaleInPlace(apples_2, 1.2, rate_func=wiggle),
                Write(plus_2),
                ScaleInPlace(bananas_2, 1.2, rate_func=wiggle),
                lag_ratio=0.2
            )
        )
        self.play(GrowFromEdge(receipt_2, UP), run_time=0.8)
        self.wait(2)

        
        
        

        
        eq1_term1 = MathTex("2", "a", color=RED_ACCENT).scale(1.2).move_to(apples_1)
        eq1_term2 = MathTex("3", "b", color=HIGHLIGHT_COLOR).scale(1.2).move_to(bananas_1)
        eq1_res = MathTex("=", "8").scale(1.2).move_to(receipt_1)

        eq2_term1 = MathTex("10", "a", color=RED_ACCENT).scale(1.2).move_to(apples_2)
        eq2_term2 = MathTex("1", "b", color=HIGHLIGHT_COLOR).scale(1.2).move_to(bananas_2)
        eq2_res = MathTex("=", "13").scale(1.2).move_to(receipt_2)

        
        bg_grid = NumberPlane(
            x_range=[-7, 7, 1], y_range=[-4, 4, 1],
            background_line_style={"stroke_color": TEAL_ACCENT, "stroke_opacity": 0.1}
        )

        self.play(FadeIn(bg_grid, run_time=2))

        
        self.play(
            ReplacementTransform(apples_1, eq1_term1),
            ReplacementTransform(bananas_1, eq1_term2),
            ReplacementTransform(receipt_1, eq1_res),
            ReplacementTransform(apples_2, eq2_term1),
            ReplacementTransform(bananas_2, eq2_term2),
            ReplacementTransform(receipt_2, eq2_res),
            FadeOut(trip1_label), FadeOut(trip2_label),
            FadeOut(shelf1), FadeOut(shelf2),
            run_time=1.5
        )

        
        target_y1 = 1.0
        target_y2 = -0.5
        col_x_eqn = [-3, -1.5, 0, 1.5, 3]

        self.play(
            
            eq1_term1.animate.move_to(RIGHT * col_x_eqn[0] + UP * target_y1),
            plus_1.animate.move_to(RIGHT * col_x_eqn[1] + UP * target_y1),
            eq1_term2.animate.move_to(RIGHT * col_x_eqn[2] + UP * target_y1),
            eq1_res[0].animate.move_to(RIGHT * col_x_eqn[3] + UP * target_y1),
            eq1_res[1].animate.move_to(RIGHT * col_x_eqn[4] + UP * target_y1),

            
            eq2_term1.animate.move_to(RIGHT * col_x_eqn[0] + UP * target_y2),
            plus_2.animate.move_to(RIGHT * col_x_eqn[1] + UP * target_y2),
            eq2_term2.animate.move_to(RIGHT * col_x_eqn[2] + UP * target_y2),
            eq2_res[0].animate.move_to(RIGHT * col_x_eqn[3] + UP * target_y2),
            eq2_res[1].animate.move_to(RIGHT * col_x_eqn[4] + UP * target_y2),
        )

        explanation = Tex(
            r"Separate \textbf{Data} (Numbers) from \textbf{Unknowns} (Variables)",
            font_size=36, color=TEAL_ACCENT
        ).to_edge(DOWN, buff=1.5)
        self.play(Write(explanation))
        self.wait(1.5)

        
        
        

        MATRIX_Y = 1.0

        matrix_lhs = Matrix([[2, 3], [10, 1]], h_buff=1.5).set_color(WHITE).move_to(LEFT * 3 + UP * MATRIX_Y)
        vector_vars = Matrix([["a"], ["b"]]).set_color(GREEN).next_to(matrix_lhs, RIGHT)
        equals = MathTex("=").next_to(vector_vars, RIGHT)
        vector_rhs = Matrix([[8], [13]]).set_color(BLUE).next_to(equals, RIGHT)

        self.play(FadeOut(explanation))

        
        self.play(
            Write(matrix_lhs.get_brackets()),
            Write(vector_vars.get_brackets()),
            Write(vector_rhs.get_brackets()),
            Write(equals)
        )

        
        
        scanner_line = Line(UP * 3, DOWN * 2, color=TEAL_ACCENT, stroke_width=4).move_to(LEFT * 6)
        scanner_glow = scanner_line.copy().set_stroke(width=15, opacity=0.3, color=TEAL_ACCENT)
        scanner = VGroup(scanner_line, scanner_glow)

        self.add(scanner)

        
        

        self.play(
            scanner.animate.move_to(RIGHT * 6),  

            
            LaggedStart(
                
                AnimationGroup(
                    eq1_term1[0].animate.move_to(matrix_lhs.get_entries()[0]),
                    eq2_term1[0].animate.move_to(matrix_lhs.get_entries()[2]),
                    Transform(eq1_term1[1], vector_vars.get_entries()[0]),  
                    Transform(eq2_term1[1], vector_vars.get_entries()[0]),
                ),
                
                AnimationGroup(
                    eq1_term2[0].animate.move_to(matrix_lhs.get_entries()[1]),
                    eq2_term2[0].animate.move_to(matrix_lhs.get_entries()[3]),
                    Transform(eq1_term2[1], vector_vars.get_entries()[1]),  
                    Transform(eq2_term2[1], vector_vars.get_entries()[1]),
                ),
                
                AnimationGroup(
                    eq1_res[1].animate.move_to(vector_rhs.get_entries()[0]),
                    eq2_res[1].animate.move_to(vector_rhs.get_entries()[1]),
                ),
                lag_ratio=0.3,  
                run_time=2.0
            ),

            
            FadeOut(plus_1, run_time=2),
            FadeOut(plus_2, run_time=2),
            FadeOut(eq1_res[0], run_time=2),
            FadeOut(eq2_res[0], run_time=2),

            run_time=2.5,
            rate_func=linear
        )

        self.play(FadeOut(scanner))

        
        lbl_matrix = Tex("Coefficient Matrix", color=YELLOW, font_size=24).next_to(matrix_lhs, DOWN)
        lbl_vector = Tex("Variable Vector", color=GREEN, font_size=24).next_to(vector_vars, DOWN)
        lbl_result = Tex("Result Vector", color=BLUE, font_size=24).next_to(vector_rhs, DOWN)

        self.play(LaggedStart(Write(lbl_matrix), Write(lbl_vector), Write(lbl_result), lag_ratio=0.2))
        self.wait(1)

        
        
        
        conclusion_box = RoundedRectangle(corner_radius=0.2, height=1.2, width=10, color=WHITE, stroke_opacity=0.5)
        conclusion = Tex(
            r"We turned a messy \textbf{Word Problem} into clean \textbf{Data Structures}.",
            font_size=32
        )
        conclusion_grp = VGroup(conclusion_box, conclusion).to_edge(DOWN, buff=0.5)

        self.play(Create(conclusion_box), Write(conclusion))
        self.wait(3)

        self.play(FadeOut(Group(topic, matrix_lhs, vector_vars, equals, vector_rhs,
                                lbl_matrix, lbl_vector, lbl_result, conclusion_grp,
                                eq1_term1[0], eq1_term2[0], eq2_term1[0], eq2_term2[0],
                                eq1_res[1], eq2_res[1], eq1_term1[1], eq1_term2[1], bg_grid)))


class WhatIsAVector(Scene):
    def construct(self):
        
        
        
        self.camera.background_color = BLACK

        
        
        COLOR_PHYS_BG = "
        COLOR_PHYS_ACCENT = "

        
        COLOR_CS_BG = "
        COLOR_CS_ACCENT = "

        
        COLOR_MATH_BG = "
        COLOR_MATH_ACCENT = "

        TEXT_COLOR = WHITE

        
        
        
        intro_title = Tex(r"\textbf{What is a Vector?}", font_size=64, color=WHITE)
        intro_sub = Tex(r"Three distinct perspectives, one concept.", font_size=32, color=GREY_A).next_to(intro_title,
                                                                                                          DOWN)

        self.play(Write(intro_title), FadeIn(intro_sub))
        self.wait(1.5)
        self.play(
            intro_title.animate.scale(0.6).to_edge(UP, buff=0.2),
            FadeOut(intro_sub)
        )

        
        separator = Line(LEFT * 7, RIGHT * 7, color=GREY_D, stroke_width=1).next_to(intro_title, DOWN, buff=0.2)
        self.play(Create(separator))

        
        
        
        
        POS_PHYS = LEFT * 3.5 + DOWN * 0.5

        
        phys_panel = RoundedRectangle(corner_radius=0.2, height=5.5, width=6, fill_color=COLOR_PHYS_BG,
                                      fill_opacity=0.5, stroke_color=COLOR_PHYS_ACCENT, stroke_width=2)
        phys_panel.move_to(POS_PHYS)

        
        p_header = Tex(r"\textbf{Physics}", color=COLOR_PHYS_ACCENT, font_size=36).next_to(phys_panel.get_top(), DOWN,
                                                                                           buff=0.3)
        p_sub = Tex("Magnitude + Direction", font_size=24, color=GREY_B).next_to(p_header, DOWN, buff=0.1)

        
        plane = NumberPlane(
            x_range=[-1, 5, 1],
            y_range=[-1, 4, 1],
            x_length=4.5,
            y_length=3.5,
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 2,
                "stroke_opacity": 0.6,
            },
            axis_config={
                "stroke_color": WHITE,
                "stroke_width": 2,
                "include_tip": False,
            }
        ).move_to(phys_panel.get_center() + DOWN * 0.3)

        
        plane.add_coordinates(font_size=16)

        
        vec_coords = [3, 2, 0]
        origin = plane.c2p(0, 0)
        tip = plane.c2p(*vec_coords)

        vector_arrow = Arrow(origin, tip, buff=0, color=YELLOW, stroke_width=6, max_tip_length_to_length_ratio=0.15)
        vec_label = MathTex(r"\vec{v}", color=YELLOW, font_size=36).next_to(vector_arrow.get_center(), UP,
                                                                            buff=0.1).shift(LEFT * 0.2)

        
        line_vertical = DashedLine(tip, plane.c2p(3, 0), color=WHITE, stroke_opacity=0.5)
        line_horizontal = DashedLine(tip, plane.c2p(0, 2), color=WHITE, stroke_opacity=0.5)

        
        label_x = MathTex("3", color=COLOR_PHYS_ACCENT, font_size=32).next_to(plane.c2p(1.5, 0), DOWN, buff=0.2)
        label_y = MathTex("2", color=COLOR_PHYS_ACCENT, font_size=32).next_to(plane.c2p(0, 1), LEFT, buff=0.2)

        physics_group = VGroup(phys_panel, p_header, p_sub, plane, vector_arrow, vec_label, line_vertical,
                               line_horizontal, label_x, label_y)

        
        self.play(FadeIn(phys_panel))
        self.play(Write(p_header), Write(p_sub))

        
        
        
        self.play(
            Create(plane, run_time=2.0, lag_ratio=0.05)
        )

        self.play(GrowArrow(vector_arrow), Write(vec_label))
        self.play(Create(line_vertical), Create(line_horizontal))
        self.play(Write(label_x), Write(label_y))
        self.wait(0.5)

        
        
        
        POS_CS = RIGHT * 3.5 + UP * 1.2

        cs_panel = RoundedRectangle(corner_radius=0.2, height=3, width=6, fill_color=COLOR_CS_BG, fill_opacity=0.5,
                                    stroke_color=COLOR_CS_ACCENT, stroke_width=2)
        cs_panel.move_to(POS_CS)

        c_header = Tex(r"\textbf{CS / Linear Algebra}", color=COLOR_CS_ACCENT, font_size=36).next_to(cs_panel.get_top(),
                                                                                                     DOWN, buff=0.2)
        c_sub = Tex("Ordered List of Numbers", font_size=24, color=GREY_B).next_to(c_header, DOWN, buff=0.1)

        
        cs_matrix = Matrix([[3], [2]],
                           v_buff=0.6,
                           h_buff=0.8,
                           bracket_h_buff=0.1,
                           element_to_mobject_config={"color": YELLOW, "font_size": 42}
                           ).next_to(c_sub, DOWN, buff=0.4)

        cs_matrix.get_brackets().set_color(COLOR_CS_ACCENT)
        brackets = cs_matrix.get_brackets()
        numbers = cs_matrix.get_entries()

        
        self.play(FadeIn(cs_panel))
        self.play(Write(c_header), Write(c_sub))
        self.play(Write(brackets))

        
        moving_3 = label_x.copy()
        moving_2 = label_y.copy()
        target_3 = numbers[0]
        target_2 = numbers[1]
        target_3.set_opacity(0)
        target_2.set_opacity(0)

        
        connector = CurvedArrow(plane.c2p(3.2, 2.2), cs_panel.get_left(), angle=-TAU / 8, color=GREY_B, stroke_width=2)
        conn_label = Tex("Extract", font_size=20, color=GREY_B).next_to(connector, UP)

        self.play(Create(connector), FadeIn(conn_label))

        
        
        packet = Dot(color=YELLOW, radius=0.08)
        self.play(MoveAlongPath(packet, connector, run_time=0.8, rate_func=linear))
        self.remove(packet)

        self.add(moving_3, moving_2)
        self.play(
            Transform(moving_3, target_3.copy().set_opacity(1).set_color(YELLOW)),
            Transform(moving_2, target_2.copy().set_opacity(1).set_color(YELLOW)),
            run_time=1.2,
            path_arc=-0.5  
        )
        self.remove(moving_3, moving_2)
        numbers.set_opacity(1)
        self.add(numbers)

        self.play(Indicate(numbers, color=WHITE))
        cs_group = VGroup(cs_panel, c_header, c_sub, brackets, numbers, connector, conn_label)

        
        
        
        POS_MATH = RIGHT * 3.5 + DOWN * 2.1

        math_panel = RoundedRectangle(corner_radius=0.2, height=3, width=6, fill_color=COLOR_MATH_BG, fill_opacity=0.5,
                                      stroke_color=COLOR_MATH_ACCENT, stroke_width=2)
        math_panel.move_to(POS_MATH)

        m_header = Tex(r"\textbf{Mathematician}", color=COLOR_MATH_ACCENT, font_size=36).next_to(math_panel.get_top(),
                                                                                                 DOWN, buff=0.2)
        m_sub = Tex("Abstract Object defined by Axioms", font_size=24, color=GREY_B).next_to(m_header, DOWN, buff=0.1)

        
        

        
        ax1_text = MathTex(r"\vec{v} + \vec{w}", color=YELLOW, font_size=32)
        ax1_arrow1 = Arrow(ORIGIN, RIGHT * 0.3 + UP * 0.1, buff=0, color=WHITE, stroke_width=2)
        ax1_arrow2 = Arrow(RIGHT * 0.3 + UP * 0.1, RIGHT * 0.6 + UP * 0.0, buff=0, color=GREY_B, stroke_width=2)

        
        ax1_icon_group = VGroup(ax1_arrow1, ax1_arrow2)
        ax1_group = VGroup(ax1_icon_group, ax1_text).arrange(RIGHT, buff=0.2)

        
        ax2_text = MathTex(r"c \cdot \vec{v}", color=YELLOW, font_size=32)
        ax2_arrow_start = Arrow(ORIGIN, RIGHT * 0.3, buff=0, color=WHITE, stroke_width=2)
        ax2_arrow_end = Arrow(ORIGIN, RIGHT * 0.6, buff=0, color=WHITE, stroke_width=2)  

        
        ax2_group = VGroup(ax2_arrow_start, ax2_text).arrange(RIGHT, buff=0.2)

        
        total_axioms = VGroup(ax1_group, ax2_group).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        total_axioms.move_to(math_panel.get_center() + DOWN * 0.2)

        
        self.play(FadeIn(math_panel))
        self.play(Write(m_header), Write(m_sub))

        
        self.play(GrowArrow(ax1_arrow1), run_time=0.5)
        self.play(GrowArrow(ax1_arrow2), Write(ax1_text), run_time=0.5)

        
        self.play(GrowArrow(ax2_arrow_start), Write(ax2_text), run_time=0.5)
        self.play(Transform(ax2_arrow_start, ax2_arrow_end), run_time=0.8)  
        self.wait(1)

        math_group = VGroup(math_panel, m_header, m_sub, ax1_arrow1, ax1_arrow2, ax1_text, ax2_arrow_start, ax2_text)

        
        
        
        
        

        trinity = Polygon(
            phys_panel.get_center(),
            cs_panel.get_center(),
            math_panel.get_center(),
            color=WHITE,
            stroke_width=2,
            stroke_opacity=0
        )

        self.play(
            phys_panel.animate.set_stroke(width=5, color=WHITE),
            cs_panel.animate.set_stroke(width=5, color=WHITE),
            math_panel.animate.set_stroke(width=5, color=WHITE),
            trinity.animate.set_stroke(opacity=0.3),
            run_time=1.0
        )

        final_text = Tex(r"Different languages, \textbf{Same Object}.", font_size=48, color=TEXT_COLOR)
        final_bg = BackgroundRectangle(final_text, color=BLACK, fill_opacity=0.9, buff=0.4)
        final_group = VGroup(final_bg, final_text).move_to(ORIGIN)

        self.play(FadeIn(final_group))
        self.wait(3)

        
        self.play(
            FadeOut(physics_group),
            FadeOut(cs_group),
            FadeOut(math_group),
            FadeOut(intro_title),
            FadeOut(separator),
            FadeOut(final_group),
            FadeOut(trinity)
        )


class GeometricView(Scene):

    def construct(self):
        
        
        
        self.camera.background_color = BLACK

        
        COLOR_VEC = YELLOW  
        COLOR_X = BLUE_C  
        COLOR_Y = RED_C  

        
        COLOR_GRID = "

        COLOR_MAG = TEAL_A  
        COLOR_DIR = ORANGE  
        COLOR_TXT = WHITE

        
        
        
        intro_title = Tex(r"\textbf{Vector Anatomy}: Magnitude \& Direction", font_size=48, color=WHITE)
        intro_sub = Tex(r"Decomposing $\vec{v}$ into components", font_size=32, color=GREY_A).next_to(intro_title, DOWN)

        self.play(Write(intro_title), FadeIn(intro_sub))
        self.wait(1.5)
        self.play(FadeOut(intro_title), FadeOut(intro_sub))

        
        
        
        
        plane = NumberPlane(
            x_range=[-4, 6, 1],
            y_range=[-4, 6, 1],
            x_length=7,
            y_length=7,
            background_line_style={
                "stroke_color": COLOR_GRID,
                "stroke_width": 2,
                "stroke_opacity": 0.5
            },
            axis_config={
                "stroke_color": GREY_B,
                "stroke_width": 2,
                "include_tip": True,
            }
        )

        
        plane.add_coordinates(font_size=20)

        
        
        graph_center = LEFT * 3.5 + DOWN * 0.5
        plane.move_to(graph_center)

        self.play(Create(plane, run_time=1.0))

        
        
        
        vec_x = 3
        vec_y = 4
        origin_pt = plane.c2p(0, 0)
        end_pt = plane.c2p(vec_x, vec_y)
        corner_pt = plane.c2p(vec_x, 0)

        
        vector = Arrow(origin_pt, end_pt, buff=0, color=COLOR_VEC, stroke_width=6)

        
        label_vec = MathTex(r"\vec{v} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}", font_size=34)
        label_vec.next_to(end_pt, UP + RIGHT, buff=0.1)
        
        label_bg = BackgroundRectangle(label_vec, color=BLACK, fill_opacity=0.6, buff=0.1)

        self.play(GrowArrow(vector), FadeIn(label_bg), Write(label_vec))
        self.wait(0.5)

        
        line_x = Line(origin_pt, corner_pt, color=COLOR_X, stroke_width=4)
        line_y = Line(corner_pt, end_pt, color=COLOR_Y, stroke_width=4)

        
        right_angle = RightAngle(line_x, line_y, length=0.4, color=WHITE, stroke_opacity=0.5, quadrant=(-1, 1))

        self.play(Create(line_x), Create(line_y), Create(right_angle))
        self.wait(0.5)

        
        
        
        
        lbl_adj = Tex("Adjacent", color=COLOR_X, font_size=24).next_to(line_x, DOWN, buff=0.15)
        lbl_opp = Tex("Opposite", color=COLOR_Y, font_size=24).next_to(line_y, RIGHT, buff=0.15)

        
        angle_rad = np.arctan2(4, 3)
        lbl_hyp = Tex("Hypotenuse", color=COLOR_VEC, font_size=24)
        lbl_hyp.move_to(plane.c2p(1.5, 2.2))  
        lbl_hyp.rotate(angle_rad)
        lbl_hyp.shift(UP * 0.2 + LEFT * 0.2)  

        self.play(Write(lbl_adj), Write(lbl_opp), FadeIn(lbl_hyp))
        self.wait(2.0)

        
        val_adj = MathTex("3", color=COLOR_X, font_size=32).next_to(line_x, DOWN, buff=0.2)
        val_opp = MathTex("4", color=COLOR_Y, font_size=32).next_to(line_y, RIGHT, buff=0.2)

        self.play(
            Transform(lbl_adj, val_adj),
            Transform(lbl_opp, val_opp),
            FadeOut(lbl_hyp)  
        )

        
        
        
        graph_group = VGroup(plane, vector, label_vec, label_bg, line_x, line_y, right_angle, lbl_adj, lbl_opp)

        
        mag_title = Tex(r"\textbf{Magnitude} (Pythagoras Theorem)", color=COLOR_MAG, font_size=40)
        mag_title.to_edge(UP, buff=1.0).to_edge(RIGHT, buff=1.0)

        mag_underline = Line(LEFT, RIGHT, color=COLOR_MAG).next_to(mag_title, DOWN, buff=0.1).scale(1.2)

        
        pyth_text = MathTex(r"(\text{Hypotenuse})^2 = (\text{Adjacent})^2 + (\text{Opposite})^2", font_size=28)
        pyth_text.next_to(mag_underline, DOWN, buff=0.5)

        
        eq_1 = MathTex(r"||\vec{v}||^2 = 3^2 + 4^2", font_size=36)
        eq_2 = MathTex(r"||\vec{v}|| = \sqrt{9 + 16}", font_size=36)
        eq_3 = MathTex(r"||\vec{v}|| = \sqrt{25}", font_size=36)
        eq_4 = MathTex(r"||\vec{v}|| = 5", color=COLOR_MAG, font_size=48)

        mag_group = VGroup(pyth_text, eq_1, eq_2, eq_3, eq_4)
        mag_group.arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        
        mag_group.next_to(mag_underline, DOWN, buff=0.5)

        
        mag_bg = BackgroundRectangle(mag_group, color=BLACK, fill_opacity=0.8, buff=0.2)

        
        brace_mag = Brace(vector, direction=np.array([-1, 1, 0]), color=COLOR_MAG, buff=0.1)
        brace_lbl = brace_mag.get_text("?").set_color(COLOR_MAG)

        self.play(Write(mag_title), Create(mag_underline))
        self.play(Create(brace_mag), Write(brace_lbl))
        self.play(FadeIn(mag_bg), Write(pyth_text))
        self.wait(1.0)

        self.play(TransformMatchingTex(pyth_text.copy(), eq_1))
        self.wait(0.5)
        self.play(TransformMatchingTex(eq_1.copy(), eq_2))
        self.wait(0.5)
        self.play(TransformMatchingTex(eq_2.copy(), eq_3))
        self.play(Write(eq_4))

        
        self.play(Indicate(eq_4, color=WHITE, scale_factor=1.1))

        final_hyp_lbl = MathTex("5", color=COLOR_MAG, font_size=36).move_to(brace_lbl)
        self.play(Transform(brace_lbl, final_hyp_lbl))
        self.wait(1.0)

        
        self.play(
            FadeOut(mag_group), FadeOut(mag_bg), FadeOut(brace_mag), FadeOut(brace_lbl),
            FadeOut(mag_title), FadeOut(mag_underline)
        )

        
        
        
        dir_title = Tex(r"\textbf{Direction} $\theta$", color=COLOR_DIR, font_size=40)
        
        dir_title.to_edge(UP, buff=1.0).to_edge(RIGHT, buff=1.0)

        dir_underline = Line(LEFT, RIGHT, color=COLOR_DIR).next_to(dir_title, DOWN, buff=0.1).scale(1.2)

        self.play(Write(dir_title), Create(dir_underline))

        
        
        self.play(graph_group.animate.shift(UP * 1.5))

        
        self.play(
            FadeOut(line_x), FadeOut(line_y), FadeOut(right_angle),
            FadeOut(lbl_adj), FadeOut(lbl_opp), FadeOut(label_vec), FadeOut(label_bg),
            FadeOut(vector)  
        )

        
        current_angle = np.arctan2(4, 3)
        theta_tracker = ValueTracker(current_angle)

        
        demo_length = 2.5
        ref_line_dynamic = Line(plane.c2p(0, 0), plane.c2p(3, 0), stroke_opacity=0)

        
        
        trace_circle = Circle(radius=demo_length, color=GREY, stroke_opacity=0.3, stroke_width=2)
        trace_circle.move_to(plane.c2p(0, 0))  
        self.play(Create(trace_circle))

        def get_arrow():
            angle = theta_tracker.get_value()
            end = plane.c2p(demo_length * np.cos(angle), demo_length * np.sin(angle))
            return Arrow(plane.c2p(0, 0), end, buff=0, color=COLOR_VEC, stroke_width=6)

        def get_arc():
            angle_val = theta_tracker.get_value()
            radius = 0.8 if angle_val < PI else 0.6
            
            return Arc(
                radius=radius,
                start_angle=0,
                angle=angle_val,
                arc_center=plane.c2p(0, 0),
                color=COLOR_DIR
            )

        def get_angle_label():
            angle_val = theta_tracker.get_value() * (180 / PI)
            arc = get_arc()
            lbl = MathTex(f"{int(angle_val)}^\circ", color=COLOR_DIR, font_size=24)
            
            if 0 <= angle_val <= 90:
                lbl.next_to(arc, RIGHT, buff=0.1).shift(UP * 0.1)
            elif 90 < angle_val <= 180:
                lbl.next_to(arc, LEFT, buff=0.1).shift(UP * 0.1)
            else:
                lbl.next_to(arc, DOWN, buff=0.1).shift(LEFT * 0.1)
            return lbl

        dynamic_arrow = always_redraw(get_arrow)
        dynamic_arc = always_redraw(get_arc)
        dynamic_label = always_redraw(get_angle_label)

        
        desc_text = Tex("", color=WHITE, font_size=32).move_to(plane.c2p(3, -2))

        self.add(dynamic_arrow, dynamic_arc, dynamic_label, desc_text)

        
        targets = [
            (25, "North East"),
            (90, "North"),
            (125, "North West"),
            (180, "West"),
            (270, "South (Tamil Nadu)")
        ]

        for deg, txt in targets:
            rad = deg * DEGREES

            
            target_pos = plane.c2p(3.5, 1)  
            if deg == 180:
                target_pos = plane.c2p(-3.5, -2)  
            elif deg == 270:
                target_pos = plane.c2p(3.5, -2)  

            self.play(
                theta_tracker.animate.set_value(rad),
                Transform(desc_text, Tex(f"{txt}", color=WHITE, font_size=36).move_to(target_pos)),
                run_time=1.5
            )
            self.wait(0.5)

        
        original_rad = np.arctan2(4, 3)
        self.play(
            theta_tracker.animate.set_value(original_rad),
            FadeOut(desc_text),
            FadeOut(trace_circle),  
            run_time=1.0
        )

        self.remove(dynamic_arrow, dynamic_arc, dynamic_label)

        
        
        new_origin = plane.c2p(0, 0)
        new_end = plane.c2p(3, 4)
        new_corner = plane.c2p(3, 0)

        final_vector = Arrow(new_origin, new_end, buff=0, color=COLOR_VEC, stroke_width=6)
        final_line_x = Line(new_origin, new_corner, color=COLOR_X, stroke_width=4)
        final_line_y = Line(new_corner, new_end, color=COLOR_Y, stroke_width=4)
        final_right_angle = RightAngle(final_line_x, final_line_y, length=0.4, color=WHITE, stroke_opacity=0.5,
                                       quadrant=(-1, 1))

        ref_line_static = Line(new_origin, new_corner, stroke_opacity=0)
        final_arc = Angle(ref_line_static, final_vector, radius=0.6, color=COLOR_DIR)
        final_angle_lbl = MathTex(r"\theta", color=COLOR_DIR, font_size=32).next_to(final_arc, RIGHT, buff=0.1).shift(
            UP * 0.1)

        
        final_val_adj = MathTex("3", color=COLOR_X, font_size=32).next_to(final_line_x, DOWN, buff=0.2)
        final_val_opp = MathTex("4", color=COLOR_Y, font_size=32).next_to(final_line_y, RIGHT, buff=0.2)

        self.play(
            GrowArrow(final_vector),
            FadeIn(final_line_x), FadeIn(final_line_y), FadeIn(final_right_angle),
            Create(final_arc), Write(final_angle_lbl),
            Write(final_val_adj), Write(final_val_opp)
        )

        final_group = VGroup(
            plane, final_vector, final_line_x, final_line_y,
            final_right_angle, final_arc, final_angle_lbl,
            final_val_adj, final_val_opp
        )
        self.play(final_group.animate.shift(DOWN * 1.5))

        
        eq_d1 = MathTex(r"\tan(\theta) = \frac{\text{Opposite}}{\text{Adjacent}}", font_size=32)
        eq_d2 = MathTex(r"\tan(\theta) = \frac{4}{3}", font_size=32)
        eq_d3 = MathTex(r"\theta = \tan^{-1}(1.33)", font_size=32)
        eq_d4 = MathTex(r"\theta \approx 53.1^\circ", color=COLOR_DIR, font_size=42)

        dir_group = VGroup(eq_d1, eq_d2, eq_d3, eq_d4)
        dir_group.arrange(DOWN, buff=0.35, aligned_edge=LEFT).next_to(dir_underline, DOWN, buff=0.5)

        
        dir_bg = BackgroundRectangle(dir_group, color=BLACK, fill_opacity=0.8, buff=0.2)

        self.play(FadeIn(dir_bg), Write(eq_d1))
        self.wait(1)
        self.play(TransformMatchingTex(eq_d1.copy(), eq_d2))
        self.wait(1)
        self.play(TransformMatchingTex(eq_d2.copy(), eq_d3))
        self.play(Write(eq_d4))

        
        self.play(Indicate(eq_d4, color=WHITE, scale_factor=1.1))

        final_angle_val = MathTex(r"53.1^\circ", color=COLOR_DIR, font_size=24).move_to(final_angle_lbl).shift(
            RIGHT * 0.3)
        self.play(Transform(final_angle_lbl, final_angle_val))
        self.wait(2)

        
        
        
        self.play(FadeOut(dir_group), FadeOut(dir_bg), FadeOut(dir_title), FadeOut(dir_underline))
        self.play(final_group.animate.move_to(ORIGIN).scale(1.2))
        self.wait(2)


class RealWorldVectors(Scene):

    def construct(self):
        
        self.camera.background_color = BLACK

        
        header = Text("VECTOR REPRESENTATION", font_size=40)
        header.to_edge(UP, buff=0.6)

        sub_header = Text("Transforming Real World Objects into Data", font_size=20, color=GRAY)
        sub_header.next_to(header, DOWN, buff=0.18)

        
        underline = Line(
            start=header.get_left() + RIGHT * 0.1,
            end=header.get_right() + LEFT * 0.1,
            stroke_width=2,
            color=GRAY_B
        ).next_to(sub_header, DOWN, buff=0.12)

        self.play(Write(header), FadeIn(sub_header, shift=DOWN * 0.12))
        self.play(Create(underline))
        self.wait(0.25)

        
        def_text = Text(
            "A vector is an ordered list of numbers representing an object's attributes.",
            font_size=20,
            color=GRAY_B,
            slant=ITALIC
        )
        def_text.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(def_text, shift=UP * 0.18))

        
        content_nudge = DOWN * 0.35

        
        
        
        house_color = TEAL

        
        p1 = [-1.5, -1, 0]
        p2 = [1.5, -1, 0]
        p3 = [1.5, 1, 0]
        p4 = [0, 2.5, 0]
        p5 = [-1.5, 1, 0]

        house_outline = Polygon(p1, p2, p3, p4, p5, color=house_color, stroke_width=4)
        door = Rectangle(width=0.8, height=1.2, color=house_color, stroke_width=4).move_to([0, -0.4, 0])
        window = Square(side_length=0.6, color=house_color, stroke_width=4).move_to([0, 0.8, 0])

        house_group = VGroup(house_outline, door, window)
        house_group.scale(0.8)
        house_group.to_edge(LEFT, buff=1.0).shift(content_nudge + DOWN * 0.05)  

        label_house = Text("Object: HOUSE", color=house_color, font_size=24)
        label_house.next_to(house_group, UP, buff=0.5)
        label_house.align_to(house_group, LEFT)

        
        self.play(Create(house_group), run_time=0.9)
        self.play(Write(label_house))

        
        data_start_x = 0
        keys_text = ["Area (sqft)", "Bedrooms", "Bathrooms", "Price ($)"]
        values_text = ["2,000", "4", "3", "500,000"]

        keys = VGroup()
        values = VGroup()

        
        base_y = 1.1
        y_step = 0.8

        for i, (k_txt, v_txt) in enumerate(zip(keys_text, values_text)):
            k = Text(k_txt, color=GRAY, font_size=24)
            v = Text(v_txt, color=house_color, font_size=24)
            k.move_to([data_start_x, base_y - i * y_step, 0])
            k.align_to([-1, 0, 0], direction=RIGHT)
            v.next_to(k, RIGHT, buff=1.0)
            
            k.shift(content_nudge)
            v.shift(content_nudge)
            keys.add(k)
            values.add(v)

        self.play(LaggedStart(*[FadeIn(k, shift=RIGHT * 0.2) for k in keys], lag_ratio=0.08))
        self.play(LaggedStart(*[Write(v) for v in values], lag_ratio=0.08))
        self.wait(0.4)

        
        vector_matrix = Matrix(
            [[0], [0], [0], [0]],
            v_buff=0.9,
            element_alignment_corner=ORIGIN
        ).set_column_colors(BLACK)

        
        vector_matrix.move_to([4.45, -0.05, 0])  

        
        brackets_house = vector_matrix.get_brackets()
        brackets_house[0].shift(LEFT * 0.38)  
        brackets_house[1].shift(RIGHT * 0.38)  
        brackets_house.set_color(WHITE)

        vec_label = MathTex(r"\vec{x} = ", font_size=36, color=house_color)
        vec_label.next_to(vector_matrix, LEFT, buff=0.1)

        
        self.play(Create(brackets_house), Write(vec_label))

        
        target_values = VGroup()
        for i, v in enumerate(values):
            t = v.copy()
            row_center = vector_matrix.get_rows()[i].get_center()
            t.move_to(row_center)
            target_values.add(t)

        
        lines = VGroup()
        for i in range(4):
            start = values[i].get_right() + RIGHT * 0.2
            end = vector_matrix.get_rows()[i].get_left() + LEFT * 0.2
            line = DashedLine(start, end, color=GRAY_D, stroke_width=2, dashed_ratio=0.5)
            lines.add(line)

        self.play(Create(lines), run_time=0.9)
        self.play(TransformFromCopy(values, target_values), run_time=1.2)
        self.wait(1.6)

        
        
        
        scene1_stuff = VGroup(
            house_group, label_house, keys, values,
            lines, vec_label, vector_matrix, target_values
        )
        self.play(FadeOut(scene1_stuff))

        new_def_text = Text(
            "Different objects have different attributes, creating different vectors.",
            font_size=20,
            color=GRAY_B,
            slant=ITALIC
        )
        new_def_text.move_to(def_text.get_center())
        self.play(Transform(def_text, new_def_text))

        
        car_color = RED_D
        c_p1 = [-2.5, -0.5, 0]
        c_p2 = [-2.5, 0.3, 0]
        c_p3 = [-1.5, 0.3, 0]
        c_p4 = [-0.8, 1.0, 0]
        c_p5 = [0.2, 1.0, 0]
        c_p6 = [1.0, 0.3, 0]
        c_p7 = [2.6, 0.1, 0]
        c_p8 = [2.6, -0.5, 0]

        car_body = Polygon(c_p1, c_p2, c_p3, c_p4, c_p5, c_p6, c_p7, c_p8,
                           color=car_color, stroke_width=4)
        wheel_1 = Circle(radius=0.45, color=car_color, stroke_width=4).move_to([-1.6, -0.5, 0])
        wheel_2 = Circle(radius=0.45, color=car_color, stroke_width=4).move_to([1.8, -0.5, 0])
        side_line = Line([-1.8, 0.0, 0], [1.0, 0.0, 0], color=car_color, stroke_width=2)

        car_group = VGroup(car_body, wheel_1, wheel_2, side_line)
        car_group.scale(0.75)
        car_group.to_edge(LEFT, buff=0.8).shift(content_nudge + DOWN * 0.05)

        label_car = Text("Object: 1960 Ford Mustang", color=car_color, font_size=24)
        label_car.next_to(car_group, UP, buff=0.5)
        label_car.align_to(car_group, LEFT)

        self.play(FadeIn(car_group, shift=LEFT * 0.18), Write(label_car))

        
        keys_text_car = ["Max Speed (km/hr)", "Price ($)", "Year", "Seats"]
        values_text_car = ["386", "45,000", "1960", "4"]

        keys_car = VGroup()
        values_car = VGroup()

        for i, (k_txt, v_txt) in enumerate(zip(keys_text_car, values_text_car)):
            k = Text(k_txt, color=GRAY, font_size=24)
            v = Text(v_txt, color=car_color, font_size=24)
            k.move_to([data_start_x, base_y - i * y_step, 0])
            k.align_to([-0.5, 0, 0], direction=RIGHT)
            k.shift(content_nudge)
            v.next_to(k, RIGHT, buff=0.8)
            v.shift(content_nudge)
            keys_car.add(k)
            values_car.add(v)

        self.play(LaggedStart(*[FadeIn(k) for k in keys_car], lag_ratio=0.08))
        self.play(LaggedStart(*[Write(v) for v in values_car], lag_ratio=0.08))

        
        vector_matrix_car = Matrix(
            [[0], [0], [0], [0]],
            v_buff=0.9
        ).set_column_colors(BLACK)

        
        vector_matrix_car.move_to([4.65, -0.05, 0])

        
        brackets_car = vector_matrix_car.get_brackets()
        brackets_car[0].shift(LEFT * 0.38)
        brackets_car[1].shift(RIGHT * 0.38)
        brackets_car.set_color(WHITE)

        vec_label_car = MathTex(r"\vec{x} = ", font_size=36, color=car_color)
        vec_label_car.next_to(vector_matrix_car, LEFT, buff=0.1)

        self.play(Create(brackets_car), Write(vec_label_car))

        target_values_car = VGroup()
        for i, v in enumerate(values_car):
            t = v.copy()
            t.move_to(vector_matrix_car.get_rows()[i].get_center())
            target_values_car.add(t)

        
        lines_car = VGroup()
        for i in range(4):
            start = values_car[i].get_right() + RIGHT * 0.2
            end = vector_matrix_car.get_rows()[i].get_left() + LEFT * 0.2
            line = DashedLine(start, end, color=GRAY_D, stroke_width=2, dashed_ratio=0.5)
            lines_car.add(line)

        self.play(Create(lines_car), run_time=0.9)

        
        highlight_box = SurroundingRectangle(keys_car[2], color=car_color, buff=0.1, stroke_width=2)
        self.play(Create(highlight_box))
        self.play(TransformFromCopy(values_car[2], target_values_car[2]))
        self.play(Uncreate(highlight_box))

        rest_indices = [0, 1, 3]
        self.play(*[TransformFromCopy(values_car[i], target_values_car[i]) for i in rest_indices], run_time=1.0)
        self.wait(0.9)

        
        
        
        self.play(
            FadeOut(car_group),
            FadeOut(label_car),
            FadeOut(keys_car),
            FadeOut(values_car),
            FadeOut(lines_car),
            FadeOut(header),
            FadeOut(sub_header),
            FadeOut(underline),
            FadeOut(def_text)
        )

        
        final_vector_group = VGroup(vec_label_car, vector_matrix_car, target_values_car)
        self.play(final_vector_group.animate.move_to(ORIGIN).scale(0.6))

        
        screen_width = 4.0
        screen_height = 3.0
        screen_rect = RoundedRectangle(corner_radius=0.2, width=screen_width, height=screen_height,
                                       color=WHITE, stroke_width=4)
        stand_leg = Rectangle(width=0.2, height=0.5, color=GRAY_B)
        stand_base = RoundedRectangle(corner_radius=0.05, width=1.5, height=0.1, color=GRAY_B)

        screen_rect.move_to(ORIGIN)
        stand_leg.next_to(screen_rect, DOWN, buff=0)
        stand_base.next_to(stand_leg, DOWN, buff=0)

        computer = VGroup(screen_rect, stand_leg, stand_base)
        self.play(Create(computer))

        
        final_vector_group.move_to(screen_rect.get_center()).shift(UP * 0.02)
        self.play(target_values_car.animate.set_color(GREEN), run_time=0.6)

        
        behind = RoundedRectangle(corner_radius=0.12, width=1.05, height=2.1, stroke_width=0, fill_opacity=0.03,
                                  fill_color=WHITE)
        behind.move_to(final_vector_group.get_center())
        self.play(FadeIn(behind, run_time=0.6))

        
        highlight_vec = SurroundingRectangle(final_vector_group, color=GREEN_A, buff=0.18, stroke_width=1.8)
        highlight_vec.set_opacity(0.6)
        self.play(Create(highlight_vec), run_time=0.7)
        self.play(FadeOut(highlight_vec), run_time=0.7)

        self.play(FadeOut(behind), run_time=0.5)

        
        scan_line = Line(
            start=[-screen_width / 2 + 0.2, screen_height / 2 - 0.2, 0],
            end=[screen_width / 2 - 0.2, screen_height / 2 - 0.2, 0],
            color=GREEN_A,
            stroke_width=4
        )
        scan_line.set_opacity(0.85)
        self.play(FadeIn(scan_line))
        self.play(scan_line.animate.move_to([0, -screen_height / 2 + 0.2, 0]), rate_func=linear, run_time=2)
        self.play(FadeOut(scan_line))

        
        quote = Text("“Reality is complex — to a machine, it is a list of numbers.”",
                     font_size=24, slant=ITALIC, color=WHITE)
        quote.next_to(computer, DOWN, buff=0.46)

        poetic_text = Text("Bridging the physical world with the digital mind.",
                           font_size=18, color=TEAL, slant=ITALIC)
        poetic_text.next_to(quote, DOWN, buff=0.22)

        self.play(Write(quote), run_time=1.2)
        self.play(FadeIn(poetic_text))
        self.wait(2.6)

        self.play(FadeOut(Group(*self.mobjects)))


class SummaryScene(Scene):
    """
    Scene 6: Recap and Conclusion
    Duration: ~1.5 Minutes
    """

    def construct(self):
        
        self.camera.background_color = BLACK

        
        title = Text(
            "SUMMARY",
            font_size=48,
            weight=BOLD,
            color=TEAL
        )
        title.to_edge(UP, buff=0.8)

        
        underline = Line(ORIGIN, RIGHT, color=TEAL, stroke_width=4)
        underline.match_width(title)
        underline.next_to(title, DOWN, buff=0.15)

        self.play(
            Write(title),
            Create(underline),
            run_time=1.5
        )

        
        
        plane = NumberPlane(
            x_range=[-1, 5],
            y_range=[-1, 4],
            x_length=4,
            y_length=3,
            axis_config={"color": GREY, "stroke_opacity": 0.5},
            background_line_style={"stroke_color": GREY, "stroke_width": 1, "stroke_opacity": 0.2}
        ).to_edge(RIGHT, buff=1).shift(DOWN * 0.5)

        
        vector_end = plane.c2p(3, 2)
        origin = plane.c2p(0, 0)

        arrow = Arrow(origin, vector_end, buff=0, color=YELLOW, stroke_width=6, max_tip_length_to_length_ratio=0.2)
        arrow_label = MathTex(r"\vec{v}", color=YELLOW).next_to(arrow, UP, buff=0.1)

        
        x_line = DashedLine(plane.c2p(3, 0), vector_end, color=BLUE_B)
        y_line = DashedLine(plane.c2p(0, 2), vector_end, color=BLUE_B)

        
        x_text = MathTex("x", color=BLUE_B, font_size=24).next_to(x_line, RIGHT, buff=0.1)
        y_text = MathTex("y", color=BLUE_B, font_size=24).next_to(y_line, UP, buff=0.1)

        
        angle = Angle(Line(origin, plane.c2p(1, 0)), arrow, radius=0.6, color=ORANGE)
        theta = MathTex(r"\theta", color=ORANGE, font_size=24).next_to(angle, RIGHT, buff=0.1).shift(UP * 0.1)

        visual_group = VGroup(plane, arrow, arrow_label, x_line, y_line, x_text, y_text, angle, theta)

        
        
        
        bullet_texts = [
            r"Vectors: Lists (CS) or Arrows (Physics).",
            r"Split into $x$ and $y$ components.",
            r"Magnitude: $\|\vec{v}\| = \sqrt{x^2 + y^2}$",
            r"Direction: $\theta = \tan^{-1}(y/x)$",
            r"Real-world modeling (velocity, force).",
        ]

        text_group = VGroup()

        for t in bullet_texts:
            
            
            bullet = Triangle(color=TEAL, fill_opacity=1).scale(0.12).rotate(-PI / 2)
            
            content = Tex(t, font_size=34, color=WHITE)
            
            line = VGroup(bullet, content).arrange(RIGHT, buff=0.3)
            
            line.shift(RIGHT * line.width / 2)
            text_group.add(line)

        
        text_group.arrange(DOWN, buff=0.6, aligned_edge=LEFT)
        text_group.to_edge(LEFT, buff=0.8).shift(DOWN * 0.5)

        
        
        

        
        text_group[0][1].set_color_by_tex("(CS)", BLUE)
        text_group[0][1].set_color_by_tex("(Physics)", GREEN)

        
        text_group[2][1].set_color_by_tex("Magnitude", YELLOW)
        text_group[3][1].set_color_by_tex("Direction", ORANGE)

        
        text_group[4][1].set_color_by_tex("velocity", YELLOW)
        text_group[4][1].set_color_by_tex("force", RED)

        

        
        self.play(Create(plane), run_time=1.5, lag_ratio=0.1)

        
        for i, item in enumerate(text_group):
            
            self.play(
                FadeIn(item, shift=RIGHT * 0.3),
                run_time=0.6
            )

            
            if i == 0:
                
                self.play(GrowArrow(arrow), Write(arrow_label))

            elif i == 1:
                
                self.play(
                    Create(x_line), Write(x_text),
                    Create(y_line), Write(y_text)
                )

            elif i == 2:
                
                self.play(Flash(arrow, color=YELLOW, flash_radius=1.5, line_length=0.2))
                self.play(Indicate(arrow_label, scale_factor=1.2))

            elif i == 3:
                
                self.play(Create(angle), Write(theta))
                
                self.play(
                    Wiggle(angle, scale_value=1.3),
                    Rotate(
                        arrow,
                        angle=PI / 12,
                        about_point=origin,
                        rate_func=there_and_back
                    ),
                    run_time=1.5
                )

            elif i == 4:
                
                self.play(Circumscribe(text_group[4], color=BLUE, fade_out=True))

            else:
                self.wait(0.5)

        self.wait(2)

        
        
        everything = VGroup(title, underline, text_group, visual_group)

        self.play(
            FadeOut(everything, shift=UP),
            run_time=1.5
        )
        self.wait(1)


class SamSciTechIntro(MovingCameraScene):

    def construct(self):

        
        self.camera.background_color = BLACK

        
        if not hasattr(self.camera, "frame"):
            raise TypeError("ERROR: This scene must inherit from 'MovingCameraScene'.")

        
        C_TEXT = WHITE
        C_HIGHLIGHT = TEAL_B
        C_ACCENT = YELLOW
        C_WARN = RED_B
        C_TECH = BLUE_B

        
        
        bg_grid = NumberPlane(
            x_range=[-20, 20], y_range=[-20, 20],
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 2,
                "stroke_opacity": 0.3
            }
        )
        self.add(bg_grid)
        
        bg_grid.add_updater(lambda m, dt: m.rotate(dt * 0.02))

        
        

        
        box = Rectangle(height=4, width=5, fill_color=BLACK, fill_opacity=0.9, stroke_color=WHITE, stroke_width=4)
        box_glow = box.copy().set_stroke(color=BLUE, width=10, opacity=0.5)
        box_label = Text("Machine Learning", font_size=40, color=WHITE).move_to(box.get_center())

        box_group = VGroup(box_glow, box, box_label)

        
        input_arrow = Arrow(LEFT * 6, LEFT * 2.5, color=C_TECH, stroke_width=6)
        output_arrow = Arrow(RIGHT * 2.5, RIGHT * 6, color=C_TECH, stroke_width=6)

        input_text = Text("Python Code", font_size=28, color=C_TECH).next_to(input_arrow, UP)
        output_text = Text("Magic?", font_size=28, color=PURPLE_B).next_to(output_arrow, UP)

        
        self.play(
            FadeIn(box_group, scale=0.5),
            run_time=1.5
        )
        self.play(
            GrowArrow(input_arrow),
            FadeIn(input_text),
            run_time=1
        )

        
        self.play(
            Flash(box, color=WHITE, flash_radius=4, num_lines=20),
            Wiggle(box_label),
            run_time=1
        )

        self.play(
            GrowArrow(output_arrow),
            FadeIn(output_text),
            run_time=1
        )
        self.wait(1)

        
        
        math_color = GREY_B
        math_1 = MathTex(r"\nabla L(\theta)", color=math_color, font_size=48)
        math_2 = MathTex(r"\int_{-\infty}^{\infty}", color=math_color, font_size=48)
        math_3 = MathTex(r"\sum_{i=1}^{n}", color=math_color, font_size=48)
        math_4 = MathTex(r"\frac{\partial y}{\partial x}", color=math_color, font_size=48)

        math_bg = VGroup(math_1, math_2, math_3, math_4).arrange_in_grid(rows=2, buff=1.5)
        math_bg.move_to(box.get_center())

        self.play(
            FadeOut(box_label),
            FadeIn(math_bg),
            box.animate.set_stroke(color=C_WARN),
            box_glow.animate.set_stroke(color=RED, opacity=0.3),
            input_text.animate.set_color(C_WARN),
            run_time=1.5
        )

        panic_text = Text("NO MATH!", font_size=70, color=C_WARN, weight=BOLD).rotate(15 * DEGREES)
        
        panic_text.add_background_rectangle(color=BLACK, opacity=0.8, buff=0.2)

        self.play(GrowFromCenter(panic_text))
        self.wait(1)

        
        self.play(
            *[FadeOut(m) for m in
              [box_group, input_arrow, output_arrow, input_text, output_text, math_bg, panic_text]],
            run_time=1
        )

        

        frame = self.camera.frame

        
        path = Line(UP * 3, DOWN * 18, color=C_TECH, stroke_width=4)
        path_glow = Line(UP * 3, DOWN * 18, color=BLUE, stroke_width=15, stroke_opacity=0.3)
        self.play(Create(path), FadeIn(path_glow))

        
        def create_step(title, icon_mobject, position_y, color):
            
            outer_dot = Dot(point=RIGHT * 0 + UP * position_y, color=color, radius=0.2)
            inner_dot = Dot(point=RIGHT * 0 + UP * position_y, color=WHITE, radius=0.08)
            dot_group = VGroup(outer_dot, inner_dot)

            
            label = Text(title, font_size=42, color=color, weight=BOLD).next_to(outer_dot, RIGHT, buff=0.6)

            
            icon_mobject.scale(0.8).next_to(label, DOWN, buff=0.5).align_to(label, LEFT)

            return dot_group, label, icon_mobject

        
        la_visual = VGroup()
        grid_mini = NumberPlane(x_range=[-2, 2], y_range=[-2, 2], x_length=3, y_length=3,
                                axis_config={"color": BLUE_A}, background_line_style={"stroke_opacity": 0.4})
        vec1 = Arrow(grid_mini.c2p(0, 0), grid_mini.c2p(1, 2), buff=0, color=YELLOW, stroke_width=4)
        vec2 = Arrow(grid_mini.c2p(0, 0), grid_mini.c2p(2, -1), buff=0, color=RED, stroke_width=4)
        la_visual.add(grid_mini, vec1, vec2)

        dot1, title1, visual1 = create_step("1. Linear Algebra", la_visual, 2.5, C_HIGHLIGHT)

        
        calc_visual = VGroup()
        axes_calc = Axes(x_range=[0, 4], y_range=[0, 4], x_length=3, y_length=2, axis_config={"color": GREY})
        curve = axes_calc.plot(lambda x: 0.5 * (x - 2) ** 2 + 1, color=BLUE)
        tangent = TangentLine(curve, alpha=0.7, length=2, color=YELLOW)
        calc_visual.add(axes_calc, curve, tangent)

        dot2, title2, visual2 = create_step("2. Calculus", calc_visual, -1.5, BLUE)

        
        prob_visual = VGroup()
        axes_prob = Axes(x_range=[-3, 3], y_range=[0, 1], x_length=3, y_length=2, tips=False,
                         axis_config={"color": GREY})
        bell = axes_prob.plot(lambda x: np.exp(-x ** 2 / 2), color=GREEN)
        particles = VGroup(
            *[Dot(radius=0.05, color=WHITE).move_to(axes_prob.c2p(np.random.normal(0, 1), 0)) for _ in range(30)])
        prob_visual.add(axes_prob, bell, particles)

        dot3, title3, visual3 = create_step("3. Prob & Stats", prob_visual, -5.5, GREEN)

        
        opt_visual = VGroup()
        axes_opt = Axes(x_range=[-2, 2], y_range=[0, 4], x_length=3, y_length=2, tips=False,
                        axis_config={"color": GREY})
        bowl = axes_opt.plot(lambda x: x ** 2, color=PURPLE)
        ball = Dot(color=YELLOW, radius=0.2).move_to(axes_opt.c2p(1.5, 1.5 ** 2))
        arrow_down = Arrow(start=ball.get_center(), end=ball.get_center() + DL * 0.5, color=YELLOW, buff=0)
        opt_visual.add(axes_opt, bowl, ball, arrow_down)

        dot4, title4, visual4 = create_step("4. Optimization", opt_visual, -9.5, PURPLE)

        
        ml_visual = VGroup()
        
        layers = [2, 3, 2]
        neurons = VGroup()
        edges = VGroup()
        node_radius = 0.15
        layer_gap = 1.0

        l1_pos = [UL * 0.5, DL * 0.5]
        l2_pos = [UP * 0.5 + RIGHT * layer_gap, RIGHT * layer_gap, DOWN * 0.5 + RIGHT * layer_gap]
        l3_pos = [UL * 0.5 + RIGHT * layer_gap * 2, DL * 0.5 + RIGHT * layer_gap * 2]

        l1_nodes = [Dot(p, radius=node_radius, color=BLUE) for p in l1_pos]
        l2_nodes = [Dot(p, radius=node_radius, color=GREEN) for p in l2_pos]
        l3_nodes = [Dot(p, radius=node_radius, color=RED) for p in l3_pos]

        all_nodes = l1_nodes + l2_nodes + l3_nodes

        
        for n1 in l1_nodes:
            for n2 in l2_nodes:
                edges.add(Line(n1.get_center(), n2.get_center(), stroke_width=1, color=WHITE, stroke_opacity=0.3))
        for n1 in l2_nodes:
            for n2 in l3_nodes:
                edges.add(Line(n1.get_center(), n2.get_center(), stroke_width=1, color=WHITE, stroke_opacity=0.3))

        neurons.add(*all_nodes)
        ml_visual.add(edges, neurons).center()

        dot5, title5, visual5 = create_step("5. Machine Learning", ml_visual, -13.5, GOLD)

        

        
        self.play(FadeIn(dot1, scale=0.5), Write(title1))
        self.play(Create(visual1), run_time=1)
        self.wait(0.5)

        
        self.play(
            frame.animate.move_to(dot2.get_center() + RIGHT * 1.5),
            FadeIn(dot2, scale=0.5), Write(title2),
            Create(visual2)
        )
        self.wait(0.5)

        
        self.play(
            frame.animate.move_to(dot3.get_center() + RIGHT * 1.5),
            FadeIn(dot3, scale=0.5), Write(title3),
            Create(visual3)
        )
        self.wait(0.5)

        
        self.play(
            frame.animate.move_to(dot4.get_center() + RIGHT * 1.5),
            FadeIn(dot4, scale=0.5), Write(title4),
            Create(visual4),
            ball.animate.move_to(axes_opt.c2p(0, 0))  
        )
        self.wait(0.5)

        
        self.play(
            frame.animate.move_to(dot5.get_center() + RIGHT * 1.5),
            FadeIn(dot5, scale=0.5), Write(title5),
            Create(visual5)
        )
        
        self.play(Indicate(visual5, color=WHITE, scale_factor=1.1, run_time=1))
        self.wait(1)

        

        
        self.play(
            FadeOut(dot1, title1, visual1, dot2, title2, visual2, dot3, title3, visual3, dot4, title4, visual4,
                    path, path_glow),
            frame.animate.move_to(visual5.get_center()).set_height(7)
        )

        
        stars = VGroup(*[
            Dot(color=random_color(), radius=np.random.random() * 0.08)
            for _ in range(80)
        ]).move_to(visual5.get_center())

        
        for star in stars:
            star.shift(np.random.random() * 5 * RIGHT + np.random.random() * 5 * UP - np.array([2.5, 2.5, 0]))

        physics_text = Text("Physics + Code", font_size=56, color=WHITE, weight=BOLD).next_to(visual5, UP, buff=1.2)

        
        self.play(
            Transform(ml_visual, stars),  
            Write(physics_text),
            run_time=2
        )

        
        self.play(
            Rotate(ml_visual, angle=PI, about_point=ml_visual.get_center()),
            run_time=3
        )

        
        self.play(FadeOut(ml_visual), FadeOut(physics_text))

        
        
        logo_circle = Circle(radius=1.5, color=C_HIGHLIGHT, stroke_width=8)
        logo_triangle = Triangle(color=BLUE, fill_opacity=0.8, fill_color=BLUE_E).scale(1.0).rotate(-30 * DEGREES)

        
        logo_glow = logo_circle.copy().set_stroke(width=20, opacity=0.3, color=C_HIGHLIGHT)

        logo_text = Text("Sam SciTech", font_size=60, font="sans-serif", weight=BOLD, color=WHITE).next_to(
            logo_circle, DOWN)

        logo_group = VGroup(logo_glow, logo_circle, logo_triangle, logo_text).center()

        self.play(
            FadeIn(logo_glow),
            DrawBorderThenFill(logo_circle),
            GrowFromCenter(logo_triangle),
            run_time=1.5
        )
        self.play(Write(logo_text))

        
        subscribe = Text("Subscribe to Understand.", font_size=32, color=C_ACCENT).next_to(logo_text, DOWN,
                                                                                           buff=0.5)
        self.play(FadeIn(subscribe, shift=UP))

        self.wait(3)
        self.play(FadeOut(logo_group), FadeOut(subscribe), FadeOut(bg_grid))


class VisualPromise(ThreeDScene):
    def construct(self):
        
        self.camera.background_color = BLACK

        
        
        old_text = Text("Old School Math", font="sans-serif", font_size=80, color=GREY_C)
        self.add_fixed_in_frame_mobjects(old_text)

        self.play(Write(old_text), run_time=1)

        
        cross = Cross(old_text, stroke_color=RED, stroke_width=15)
        self.add_fixed_in_frame_mobjects(cross)

        self.play(Create(cross), run_time=0.5)
        self.wait(0.5)

        
        self.play(
            FadeOut(old_text),
            FadeOut(cross),
            run_time=1
        )

        
        
        self.move_camera(phi=75 * DEGREES, theta=-30 * DEGREES, zoom=0.8, run_time=2.5)

        
        axes = ThreeDAxes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            z_range=[-4, 4, 1],
            x_length=10,
            y_length=10,
            z_length=6,
            axis_config={"include_tip": True, "stroke_width": 2}
        )
        
        axes.get_axis(0).set_color(TEAL)  
        axes.get_axis(1).set_color(MAROON)  
        axes.get_axis(2).set_color(BLUE)  

        self.play(Create(axes), run_time=1.5)

        
        
        grid = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 2,
                "stroke_opacity": 0.3
            }
        )
        self.play(FadeIn(grid), run_time=1)

        
        label_matrix = Text("Matrix [[1, 1], [0, 1]]", font_size=36, color=WHITE).to_corner(UL)
        label_trans = Text("Linear Transformation", font_size=36, color=YELLOW).to_corner(UL)

        self.add_fixed_in_frame_mobjects(label_matrix)
        self.play(Write(label_matrix))

        
        
        
        matrix = [[1, 1], [0, 1]]

        self.play(
            ApplyMatrix(matrix, grid),
            ReplacementTransform(label_matrix, label_trans),
            run_time=3
        )
        self.wait(1)
        self.play(FadeOut(label_trans))

        
        
        vectors = VGroup()
        for i in range(50):
            
            x = np.random.uniform(-5, 5)
            y = np.random.uniform(-5, 5)
            pos = np.array([x, y, 0.1])  

            
            angle = np.arctan2(y, x) + PI / 2

            
            arrow = Arrow(
                start=ORIGIN,
                end=RIGHT * 0.6,
                buff=0,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.3
            )
            arrow.shift(pos)
            arrow.rotate(angle, about_point=pos)

            
            dist = np.linalg.norm(pos)
            
            alpha = np.clip(dist / 6.0, 0, 1)
            color = interpolate_color(YELLOW, RED, alpha)
            arrow.set_color(color)

            vectors.add(arrow)

        self.play(LaggedStart(*[GrowArrow(v) for v in vectors], lag_ratio=0.05))

        
        

        final_text = Text("Geometric Intuition", font_size=60, weight=BOLD, color=WHITE)
        final_text.add_background_rectangle(color=BLACK, opacity=0.6, buff=0.2)
        self.add_fixed_in_frame_mobjects(final_text)

        self.play(
            FadeIn(final_text, scale=0.5),
            Rotate(vectors, angle=PI, about_point=ORIGIN, rate_func=smooth),  
            
            self.camera.theta_tracker.animate.increment_value(-60 * DEGREES),
            run_time=5
        )

        self.wait(2)
