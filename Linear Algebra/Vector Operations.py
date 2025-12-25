from manim import *


class VectorOperations(Scene):
    def construct(self):
        
        self.camera.background_color = BLACK

        
        VEC_A_COLOR = TEAL_C  
        VEC_B_COLOR = YELLOW_C  
        RES_COLOR = MAROON_B  
        COMP_X_COLOR = BLUE_E  
        COMP_Y_COLOR = RED_E  
        BASIS_I_COLOR = GREEN_C
        BASIS_J_COLOR = RED_C
        AXIS_COLOR = GREY_C
        GRID_COLOR = GREY_E
        TEXT_MAIN = WHITE

        
        def get_vec(coords, color, plane, label_text=None):
            """Creates a vector with an optional label."""
            origin = plane.c2p(0, 0, 0)
            target = plane.c2p(*coords)
            vec = Arrow(origin, target, buff=0, color=color, stroke_width=4, max_tip_length_to_length_ratio=0.15)
            if label_text:
                label = MathTex(label_text, color=color, font_size=36).next_to(vec.get_end(), UP + RIGHT, buff=0.1)
                return VGroup(vec, label)
            return VGroup(vec)

        def get_dashed_lines(coords, color, plane):
            """Creates dashed projection lines to axes."""
            origin = plane.c2p(0, 0, 0)
            point = plane.c2p(*coords)
            x_proj = plane.c2p(coords[0], 0, 0)

            line_vert = DashedLine(x_proj, point, color=color, stroke_width=2, dash_length=0.1)
            line_horiz = DashedLine(plane.c2p(0, coords[1], 0), point, color=color, stroke_width=2, dash_length=0.1)
            return VGroup(line_vert, line_horiz)

        
        
        

        title = Text("Linear Algebra Foundations", font_size=56, weight=BOLD).to_edge(UP, buff=1)
        subtitle = Text("The mathematics powering Neural Networks", font_size=28, color=GREY_B).next_to(title, DOWN)

        
        equation = MathTex(
            r"\alpha", r"\vec{u}", "+", r"\beta", r"\vec{v}",
            font_size=72
        ).move_to(ORIGIN)
        equation[0].set_color(VEC_A_COLOR)  
        equation[1].set_color(VEC_A_COLOR)  
        equation[3].set_color(VEC_B_COLOR)  
        equation[4].set_color(VEC_B_COLOR)  

        
        op_names = VGroup(
            Text("Vector Addition", font_size=32, color=VEC_A_COLOR),
            Text("&", font_size=32, color=WHITE),
            Text("Scalar Multiplication", font_size=32, color=VEC_B_COLOR)
        ).arrange(RIGHT, buff=0.2).next_to(equation, DOWN, buff=0.5)

        
        self.play(Write(title), FadeIn(subtitle, shift=UP))
        self.play(GrowFromCenter(equation), run_time=1.5)
        self.play(FadeIn(op_names, shift=UP))
        self.wait(2)

        self.play(FadeOut(Group(title, subtitle, equation, op_names)))

        
        
        

        
        plane = NumberPlane(
            x_range=[-2, 8, 1], y_range=[-2, 6, 1],
            background_line_style={"stroke_color": GRID_COLOR, "stroke_width": 1, "stroke_opacity": 0.3},
            axis_config={"stroke_color": AXIS_COLOR, "include_tip": True}
        ).scale(0.8).to_edge(LEFT, buff=1)

        self.play(Create(plane, run_time=2, lag_ratio=0.1))

        
        v1_coords = [3, 2, 0]
        v1_group = get_vec(v1_coords, VEC_A_COLOR, plane, r"\vec{v}")
        v1_lines = get_dashed_lines(v1_coords, VEC_A_COLOR, plane)

        self.play(GrowArrow(v1_group[0]), Write(v1_group[1]))
        self.play(Create(v1_lines))

        
        v2_coords = [1, 3, 0]
        v2_group = get_vec(v2_coords, VEC_B_COLOR, plane, r"\vec{w}")
        v2_lines = get_dashed_lines(v2_coords, VEC_B_COLOR, plane)

        self.play(GrowArrow(v2_group[0]), Write(v2_group[1]))
        self.play(Create(v2_lines))

        
        brace_x1 = BraceBetweenPoints(plane.c2p(0, 0), plane.c2p(3, 0), DOWN, buff=0.1).set_color(VEC_A_COLOR)
        label_x1 = MathTex("3", color=VEC_A_COLOR, font_size=24).next_to(brace_x1, DOWN, buff=0.1)

        brace_x2_origin = BraceBetweenPoints(plane.c2p(0, 0), plane.c2p(1, 0), DOWN, buff=0.4).set_color(VEC_B_COLOR)
        label_x2_origin = MathTex("1", color=VEC_B_COLOR, font_size=24).next_to(brace_x2_origin, DOWN, buff=0.1)

        self.play(GrowFromCenter(brace_x1), FadeIn(label_x1))
        self.play(GrowFromCenter(brace_x2_origin), FadeIn(label_x2_origin))

        
        
        
        brace_y1 = BraceBetweenPoints(plane.c2p(0, 0), plane.c2p(0, 2), LEFT, buff=0.1).set_color(VEC_A_COLOR)
        label_y1 = MathTex("2", color=VEC_A_COLOR, font_size=24).next_to(brace_y1, LEFT, buff=0.1)

        
        brace_y2_origin = BraceBetweenPoints(plane.c2p(0, 0), plane.c2p(0, 3), LEFT, buff=0.4).set_color(VEC_B_COLOR)
        label_y2_origin = MathTex("3", color=VEC_B_COLOR, font_size=24).next_to(brace_y2_origin, LEFT, buff=0.1)

        self.play(GrowFromCenter(brace_y1), FadeIn(label_y1))
        self.play(GrowFromCenter(brace_y2_origin), FadeIn(label_y2_origin))
        self.wait(0.5)

        
        v2_ghost = v2_group[0].copy().set_opacity(0.3)
        self.add(v2_ghost)

        shift_vec = plane.c2p(*v1_coords) - plane.c2p(0, 0, 0)

        self.play(
            v2_group.animate.shift(shift_vec),
            v2_lines.animate.shift(shift_vec),
            run_time=1.5,
            path_arc=0.2
        )

        
        
        brace_x2_shifted = BraceBetweenPoints(plane.c2p(3, 0), plane.c2p(4, 0), DOWN, buff=0.1).set_color(VEC_B_COLOR)
        self.play(
            Transform(brace_x2_origin, brace_x2_shifted),
            label_x2_origin.animate.next_to(brace_x2_shifted, DOWN, buff=0.1)
        )
        
        
        brace_y2_shifted = BraceBetweenPoints(plane.c2p(0, 2), plane.c2p(0, 5), LEFT, buff=0.1).set_color(VEC_B_COLOR)
        self.play(
            Transform(brace_y2_origin, brace_y2_shifted),
            label_y2_origin.animate.next_to(brace_y2_shifted, LEFT, buff=0.1)
        )

        
        brace_x_total = BraceBetweenPoints(plane.c2p(0, 0), plane.c2p(4, 0), DOWN, buff=0.7).set_color(RES_COLOR)
        label_x_total = MathTex("3 + 1 = 4", color=RES_COLOR, font_size=24).next_to(brace_x_total, DOWN, buff=0.1)

        brace_y_total = BraceBetweenPoints(plane.c2p(0, 0), plane.c2p(0, 5), LEFT, buff=0.7).set_color(RES_COLOR)
        label_y_total = MathTex("2 + 3 = 5", color=RES_COLOR, font_size=24).next_to(brace_y_total, LEFT, buff=0.1)

        self.play(
            TransformFromCopy(VGroup(brace_x1, brace_x2_origin), brace_x_total), Write(label_x_total),
            TransformFromCopy(VGroup(brace_y1, brace_y2_origin), brace_y_total), Write(label_y_total)
        )

        
        res_coords = [4, 5, 0]
        res_group = get_vec(res_coords, RES_COLOR, plane, r"\vec{v}+\vec{w}")
        res_lines = get_dashed_lines(res_coords, RES_COLOR, plane)

        self.play(GrowArrow(res_group[0]), Write(res_group[1]))
        self.play(Create(res_lines))

        
        algebra_box = RoundedRectangle(height=4, width=4.5, corner_radius=0.2, fill_color=BLACK, fill_opacity=0.8,
                                       stroke_color=GREY_B, stroke_width=1).to_edge(RIGHT, buff=0.5)

        matrix_eq = MathTex(
            r"\begin{bmatrix} 3 \\ 2 \end{bmatrix}",
            "+",
            r"\begin{bmatrix} 1 \\ 3 \end{bmatrix}",
            "=",
            r"\begin{bmatrix} 3+1 \\ 2+3 \end{bmatrix}",
            "=",
            r"\begin{bmatrix} 4 \\ 5 \end{bmatrix}"
        ).scale(0.8).move_to(algebra_box)

        matrix_eq[0].set_color(VEC_A_COLOR)
        matrix_eq[2].set_color(VEC_B_COLOR)
        matrix_eq[4][1:2].set_color(VEC_A_COLOR)  
        matrix_eq[4][3:4].set_color(VEC_B_COLOR)  
        matrix_eq[4][5:6].set_color(VEC_A_COLOR)  
        matrix_eq[4][7:8].set_color(VEC_B_COLOR)  
        matrix_eq[6].set_color(RES_COLOR)

        self.play(Create(algebra_box), Write(matrix_eq[0:4]))
        self.play(Write(matrix_eq[4]))
        self.play(Write(matrix_eq[5:]))

        self.wait(2)

        
        self.play(
            FadeOut(Group(v1_group, v1_lines, v2_group, v2_lines, v2_ghost, res_group, res_lines,
                          brace_x1, label_x1, brace_x2_origin, label_x2_origin, brace_x_total, label_x_total,
                          brace_y1, label_y1, brace_y2_origin, label_y2_origin, brace_y_total, label_y_total,
                          algebra_box, matrix_eq))
        )

        
        
        

        
        v1_group = get_vec([3, 2, 0], VEC_A_COLOR, plane, r"\vec{v}")
        v2_group = get_vec([1, 3, 0], VEC_B_COLOR, plane, r"\vec{w}")
        self.play(GrowArrow(v1_group[0]), GrowArrow(v2_group[0]), Write(v1_group[1]), Write(v2_group[1]))

        
        sub_box = RoundedRectangle(height=4, width=5, corner_radius=0.2, fill_color=BLACK, fill_opacity=0.8,
                                   stroke_color=GREY_B, stroke_width=1).to_edge(RIGHT, buff=0.5)
        sub_title = Text("Subtraction", font_size=36).next_to(sub_box.get_top(), DOWN, buff=0.5)
        sub_desc = MathTex(r"\vec{v} - \vec{w} = \vec{v} + (-\vec{w})", font_size=32).next_to(sub_title, DOWN)

        self.play(Create(sub_box), Write(sub_title), Write(sub_desc))

        
        neg_w_coords = [-1, -3, 0]
        neg_w_group = get_vec(neg_w_coords, VEC_B_COLOR, plane, r"-\vec{w}")

        self.play(
            Transform(v2_group[0], neg_w_group[0], path_arc=1),
            Transform(v2_group[1], neg_w_group[1], path_arc=1)
        )

        
        self.play(v2_group.animate.shift(shift_vec), path_arc=0.2)

        
        sub_res_coords = [2, -1, 0]
        sub_res_group = get_vec(sub_res_coords, RES_COLOR, plane, r"\vec{v}-\vec{w}")
        sub_res_lines = get_dashed_lines(sub_res_coords, RES_COLOR, plane)

        self.play(GrowArrow(sub_res_group[0]), Write(sub_res_group[1]))
        self.play(Create(sub_res_lines))

        
        sub_eq = MathTex(
            r"\begin{bmatrix} 3 \\ 2 \end{bmatrix}",
            "-",
            r"\begin{bmatrix} 1 \\ 3 \end{bmatrix}",
            "=",
            r"\begin{bmatrix} 3-1 \\ 2-3 \end{bmatrix}",
            "=",
            r"\begin{bmatrix} 2 \\ -1 \end{bmatrix}"
        ).scale(0.7).next_to(sub_desc, DOWN, buff=0.8)

        sub_eq[0].set_color(VEC_A_COLOR)
        sub_eq[2].set_color(VEC_B_COLOR)
        sub_eq[4][1:2].set_color(VEC_A_COLOR)
        sub_eq[4][3:4].set_color(VEC_B_COLOR)
        sub_eq[4][5:6].set_color(VEC_A_COLOR)
        sub_eq[4][7:8].set_color(VEC_B_COLOR)
        sub_eq[6].set_color(RES_COLOR)

        self.play(Write(sub_eq))
        self.wait(2)

        self.play(
            FadeOut(Group(v1_group, v2_group, sub_res_group, sub_res_lines, sub_box, sub_title, sub_desc, sub_eq)))

        
        
        

        base_coords = [2, 1, 0]
        base_vec = get_vec(base_coords, VEC_A_COLOR, plane, r"\vec{v}")
        base_vec_ghost = base_vec[0].copy().set_opacity(0.3)
        self.play(GrowArrow(base_vec[0]), Write(base_vec[1]), Create(base_vec_ghost))

        scale_box = RoundedRectangle(height=3, width=4, corner_radius=0.2, fill_color=BLACK, fill_opacity=0.8,
                                     stroke_color=GREY_B, stroke_width=1).to_edge(RIGHT, buff=0.5).shift(UP)
        scale_title = Text("Scalar Multiplication", font_size=36).next_to(scale_box.get_top(), DOWN, buff=0.3)
        self.play(Create(scale_box), Write(scale_title))

        
        scales = [2, 0.5, -1]
        labels = ["2", "0.5", "-1"]

        prev_alg_label = None

        for scale, label in zip(scales, labels):
            new_coords = [base_coords[0] * scale, base_coords[1] * scale, 0]

            
            alg_label = MathTex(f"{label} \\cdot \\vec{{v}}", color=VEC_A_COLOR).next_to(scale_title, DOWN, buff=0.5)

            
            new_arrow = Arrow(
                plane.c2p(0, 0), plane.c2p(*new_coords),
                buff=0, color=VEC_A_COLOR, stroke_width=4, max_tip_length_to_length_ratio=0.15
            )

            
            if scale < 0:
                new_label_pos = new_arrow.get_end() + DOWN + LEFT
            else:
                new_label_pos = new_arrow.get_end() + UP + RIGHT

            
            anims = [
                Transform(base_vec[0], new_arrow),
                base_vec[1].animate.move_to(new_label_pos)
            ]

            if prev_alg_label:
                anims.append(ReplacementTransform(prev_alg_label, alg_label))
            else:
                anims.append(FadeIn(alg_label))

            self.play(*anims, run_time=1.5)
            self.wait(1)

            prev_alg_label = alg_label

        self.play(FadeOut(Group(base_vec, base_vec_ghost, scale_box, scale_title, prev_alg_label)))

        
        
        

        
        i_hat = get_vec([1, 0, 0], BASIS_I_COLOR, plane, r"\hat{i}")
        j_hat = get_vec([0, 1, 0], BASIS_J_COLOR, plane, r"\hat{j}")

        self.play(GrowArrow(i_hat[0]), Write(i_hat[1]))
        self.play(GrowArrow(j_hat[0]), Write(j_hat[1]))
        self.play(i_hat[0].animate.set_stroke(width=6, opacity=0.8), j_hat[0].animate.set_stroke(width=6, opacity=0.8),
                  rate_func=there_and_back, run_time=1)

        comb_box = RoundedRectangle(height=3, width=4.5, corner_radius=0.2, fill_color=BLACK, fill_opacity=0.8,
                                    stroke_color=GREY_B, stroke_width=1).to_edge(RIGHT, buff=0.5).shift(UP)
        comb_title = Text("Linear Combinations", font_size=36).next_to(comb_box.get_top(), DOWN, buff=0.3)

        
        comb_eq = MathTex(
            r"3\hat{i}", "+", r"2\hat{j}", "=", r"\vec{v}",
            font_size=32
        ).next_to(comb_title, DOWN)

        comb_eq[0].set_color(BASIS_I_COLOR)
        comb_eq[2].set_color(BASIS_J_COLOR)
        comb_eq[4].set_color(RES_COLOR)

        self.play(Create(comb_box), Write(comb_title), Write(comb_eq))

        
        i_scaled_coords = [3, 0, 0]
        i_scaled = get_vec(i_scaled_coords, BASIS_I_COLOR, plane)

        
        j_scaled_coords = [0, 2, 0]
        j_scaled = get_vec(j_scaled_coords, BASIS_J_COLOR, plane)

        self.play(
            Transform(i_hat[0], i_scaled[0]),
            i_hat[1].animate.next_to(plane.c2p(*i_scaled_coords), DOWN),
            Transform(j_hat[0], j_scaled[0]),
            j_hat[1].animate.next_to(plane.c2p(*j_scaled_coords), LEFT)
        )

        
        parallelogram = Polygon(
            plane.c2p(0, 0), plane.c2p(*i_scaled_coords),
            plane.c2p(3, 2), plane.c2p(*j_scaled_coords),
            color=GREY, fill_opacity=0.2, stroke_width=2
        )
        self.play(Create(parallelogram))

        
        shift_amt = plane.c2p(*i_scaled_coords) - plane.c2p(0, 0)

        self.play(
            j_hat[0].animate.shift(shift_amt),
            j_hat[1].animate.shift(shift_amt)
        )

        
        final_vec = get_vec([3, 2, 0], RES_COLOR, plane, r"\vec{v}")
        self.play(GrowArrow(final_vec[0]), Write(final_vec[1]))

        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))