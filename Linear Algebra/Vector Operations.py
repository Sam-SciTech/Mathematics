from manim import *


class VectorOperations(MovingCameraScene):
    def construct(self):

        self.camera.frame.save_state()
        self.camera.frame.shift(UP * 2).set(width=16)
        self.camera.background_color = BLACK

        
        
        grid = NumberPlane(
            x_range=[-20, 20, 1],
            y_range=[-20, 20, 1],
            background_line_style={
                "stroke_color": GREY_C,
                "stroke_width": 1,
                "stroke_opacity": 0.4
            },
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
                "include_tip": False,
            }
        ).add_coordinates()

        self.play(Write(grid, lag_ratio=0.01), run_time=2)

        
        def create_vector(coords, color, label_text=None, label_pos=UP):
            vec = Vector(coords, color=color, stroke_width=6, tip_length=0.25)
            if label_text:
                label = MathTex(label_text, color=color).next_to(vec.get_end(), label_pos, buff=0.2)
                label.add_background_rectangle(color=BLACK, opacity=0.7, buff=0.1)
                return VGroup(vec, label)
            return vec

        def create_header(text):
            header = Text(text, font="Consolas", font_size=40, color=WHITE)
            header.add_background_rectangle(color=BLACK, opacity=0.9, buff=0.2)
            header.add_updater(lambda m: m.move_to(self.camera.frame.get_edge_center(UP) + DOWN * 0.8))
            return header

        
        def show_component_breakdown(vec_group, coords, color, position_quadrant=UR):
            vec = vec_group[0]
            
            x_end = [coords[0], 0, 0]
            y_end = [0, coords[1], 0]
            target = [coords[0], coords[1], 0]

            x_proj = DashedLine(x_end, target, color=color, stroke_opacity=0.5)
            y_proj = DashedLine(y_end, target, color=color, stroke_opacity=0.5)

            
            coord_text = f"\\begin{{bmatrix}} {coords[0]} \\\\ {coords[1]} \\end{{bmatrix}}"
            label = MathTex(coord_text, color=color, font_size=32)  
            label.next_to(vec.get_end(), position_quadrant, buff=0.2)
            label.add_background_rectangle(color=BLACK, opacity=0.8)

            
            self.play(
                self.camera.frame.animate.scale(0.85).move_to(vec.get_center()),
                Create(x_proj),
                Create(y_proj),
                FadeIn(label),
                run_time=0.8
            )

            
            self.play(Flash(vec.get_end(), color=color, line_length=0.2, num_lines=4), run_time=0.3)
            self.wait(0.5)

            
            self.play(
                FadeOut(x_proj), FadeOut(y_proj), FadeOut(label),
                Restore(self.camera.frame),  
                run_time=0.8
            )

        
        
        

        header_1 = create_header("Vector Addition")
        self.play(FadeIn(header_1))

        r_coords = [3, 2, 0]
        s_coords = [-1, 2, 0]

        vec_r_group = create_vector(r_coords, YELLOW, "\\vec{r}", RIGHT + DOWN)
        vec_r = vec_r_group[0]

        vec_s_group = create_vector(s_coords, BLUE, "\\vec{s}", LEFT)
        vec_s = vec_s_group[0]

        
        self.play(Create(vec_r_group), run_time=1.0)
        show_component_breakdown(vec_r_group, r_coords, YELLOW, UR)

        
        self.play(Create(vec_s_group), run_time=1.0)
        show_component_breakdown(vec_s_group, s_coords, BLUE, UL)

        
        s_ghost = vec_s.copy().set_color(GREY).set_opacity(0.3)
        self.add(s_ghost)

        
        self.play(
            vec_s_group.animate.shift(vec_r.get_end()),
            run_time=2,
            rate_func=smooth
        )
        self.play(Flash(vec_r.get_end(), color=WHITE, flash_radius=0.5, run_time=0.5))

        
        core_dot = Dot(color=WHITE, radius=0.08)
        glow_dot = Dot(color=WHITE, radius=0.2).set_opacity(0.3)
        dot_group = VGroup(core_dot, glow_dot)

        path1 = Line(ORIGIN, vec_r.get_end())
        final_tip = vec_r.get_end() + np.array(s_coords)
        path2 = Line(vec_r.get_end(), final_tip)

        self.add(dot_group)
        trace = TracedPath(core_dot.get_center, stroke_color=WHITE, stroke_width=4, dissipating_time=1.5)
        self.add(trace)

        self.play(MoveAlongPath(dot_group, path1), run_time=1.0)
        self.play(MoveAlongPath(dot_group, path2), run_time=1.0)

        
        result_coords = [r_coords[0] + s_coords[0], r_coords[1] + s_coords[1], 0]
        vec_result_group = create_vector(result_coords, PINK, "\\vec{r} + \\vec{s}", LEFT)

        
        
        self.play(
            self.camera.frame.animate.shift(UP * 2).set(width=18),
            run_time=1.5
        )
        
        self.camera.frame.save_state()

        self.play(GrowArrow(vec_result_group[0]))
        self.play(Write(vec_result_group[1]))

        self.play(
            Flash(vec_result_group[0].get_end(), color=PINK, flash_radius=0.5),
            Wiggle(vec_result_group[1], scale_value=1.2, rotation_angle=0.05 * TAU)
        )

        
        show_component_breakdown(vec_result_group, result_coords, PINK, UR)

        
        equation = MathTex(
            "\\begin{bmatrix} 3 \\\\ 2 \\end{bmatrix}",
            "+",
            "\\begin{bmatrix} -1 \\\\ 2 \\end{bmatrix}",
            "=",
            "\\begin{bmatrix} 2 \\\\ 4 \\end{bmatrix}"
        )
        equation[0][1].set_color(YELLOW);
        equation[0][2].set_color(YELLOW)
        equation[2][1:3].set_color(BLUE);
        equation[2][3].set_color(BLUE)
        equation[4][1].set_color(PINK);
        equation[4][2].set_color(PINK)

        bg_rect = SurroundingRectangle(equation, color=WHITE, fill_color=BLACK, fill_opacity=0.8, corner_radius=0.2)
        equation_group = VGroup(bg_rect, equation)

        
        equation_group.add_updater(lambda m: m.move_to(self.camera.frame.get_corner(UL) + DOWN * 2 + RIGHT * 3))

        self.play(FadeIn(equation_group))
        self.wait(2)

        
        self.play(
            FadeOut(vec_r_group), FadeOut(vec_s_group), FadeOut(vec_result_group),
            FadeOut(s_ghost), FadeOut(dot_group), FadeOut(trace), FadeOut(equation_group),
            FadeOut(header_1)
        )

        
        
        

        header_2 = create_header("Scalar Multiplication")
        self.play(FadeIn(header_2))

        a_coords = [3, 1, 0]
        vec_a_group = create_vector(a_coords, YELLOW, "\\vec{a}", DOWN)
        vec_a = vec_a_group[0]
        label_a = vec_a_group[1]

        self.play(Create(vec_a_group))
        show_component_breakdown(vec_a_group, a_coords, YELLOW, DR)

        
        self.play(self.camera.frame.animate(rate_func=smooth).shift(UP * 2 + RIGHT * 2))

        scaled_2_coords = [6, 2, 0]
        vec_2a = Vector(scaled_2_coords, color=YELLOW, stroke_width=6, tip_length=0.25)
        label_2a = MathTex("2\\vec{a}", color=YELLOW).next_to(vec_2a.get_end(), DOWN).add_background_rectangle(BLACK,
                                                                                                               0.7)

        dash_x = DashedLine([6, 0, 0], [6, 2, 0], color=YELLOW, stroke_opacity=0.5)
        dash_y = DashedLine([0, 2, 0], [6, 2, 0], color=YELLOW, stroke_opacity=0.5)

        calc_text_2 = MathTex(
            "2 \\cdot \\begin{bmatrix} 3 \\\\ 1 \\end{bmatrix} = \\begin{bmatrix} 6 \\\\ 2 \\end{bmatrix}")
        calc_text_2.set_color_by_tex("3", YELLOW).set_color_by_tex("1", YELLOW).set_color_by_tex("6",
                                                                                                 YELLOW).set_color_by_tex(
            "2", YELLOW)
        bg_2 = SurroundingRectangle(calc_text_2, color=WHITE, fill_color=BLACK, fill_opacity=0.8)
        calc_group_2 = VGroup(bg_2, calc_text_2)
        calc_group_2.add_updater(lambda m: m.move_to(self.camera.frame.get_corner(UL) + DOWN * 2.5 + RIGHT * 3.5))

        self.play(
            Transform(vec_a, vec_2a),
            Transform(label_a, label_2a),
            FadeIn(calc_group_2),
            Create(dash_x), Create(dash_y)
        )
        self.wait(1.5)
        self.play(FadeOut(dash_x), FadeOut(dash_y))

        
        self.play(self.camera.frame.animate(rate_func=smooth).move_to(UP * 1 + RIGHT * 1).set(width=10))

        scaled_half_coords = [1.5, 0.5, 0]
        vec_half_a = Vector(scaled_half_coords, color=YELLOW, stroke_width=6, tip_length=0.25)
        label_half_a = MathTex("0.5\\vec{a}", color=YELLOW).next_to(vec_half_a.get_end(),
                                                                    DOWN).add_background_rectangle(BLACK, 0.7)

        calc_text_div = MathTex(
            "0.5 \\cdot \\begin{bmatrix} 3 \\\\ 1 \\end{bmatrix} = \\begin{bmatrix} 1.5 \\\\ 0.5 \\end{bmatrix}")
        calc_text_div.set_color_by_tex("3", YELLOW).set_color_by_tex("1", YELLOW).set_color_by_tex("1.5",
                                                                                                   YELLOW).set_color_by_tex(
            "0.5", YELLOW)

        bg_div = SurroundingRectangle(calc_text_div, color=WHITE, fill_color=BLACK, fill_opacity=0.8)
        calc_group_div = VGroup(bg_div, calc_text_div)
        calc_group_div.add_updater(lambda m: m.move_to(self.camera.frame.get_corner(UL) + DOWN * 2.5 + RIGHT * 3.5))

        self.play(
            FadeOut(calc_group_2),
            Transform(vec_a, vec_half_a),
            Transform(label_a, label_half_a),
            FadeIn(calc_group_div)
        )
        self.wait(1.5)

        
        self.play(self.camera.frame.animate(rate_func=smooth).move_to(DOWN * 1 + LEFT * 1).set(width=14))

        scaled_neg_coords = [-3, -1, 0]
        vec_neg_a = Vector(scaled_neg_coords, color=RED, stroke_width=6, tip_length=0.25)
        label_neg_a = MathTex("-1\\vec{a}", color=RED).next_to(vec_neg_a.get_end(), UP).add_background_rectangle(BLACK,
                                                                                                                 0.7)

        calc_text_neg = MathTex(
            "-1 \\cdot \\begin{bmatrix} 3 \\\\ 1 \\end{bmatrix} = \\begin{bmatrix} -3 \\\\ -1 \\end{bmatrix}")
        calc_text_neg.set_color_by_tex("3", YELLOW).set_color_by_tex("1", YELLOW)
        calc_text_neg.set_color_by_tex("-3", RED).set_color_by_tex("-1", RED)

        bg_neg = SurroundingRectangle(calc_text_neg, color=WHITE, fill_color=BLACK, fill_opacity=0.8)
        calc_group_neg = VGroup(bg_neg, calc_text_neg)
        calc_group_neg.add_updater(lambda m: m.move_to(self.camera.frame.get_corner(UL) + DOWN * 2.5 + RIGHT * 3.5))

        self.play(
            FadeOut(calc_group_div),
            Transform(vec_a, vec_neg_a),
            Transform(label_a, label_neg_a),
            FadeIn(calc_group_neg)
        )
        self.wait(2)

        
        self.play(
            FadeOut(vec_a), FadeOut(label_a), FadeOut(calc_group_neg), FadeOut(header_2),
            self.camera.frame.animate.move_to(UP * 1.5).set(width=16)  
        )
        self.play(Restore(self.camera.frame))

        
        
        

        header_3 = create_header("Vector Subtraction")
        self.play(FadeIn(header_3))

        vec_r_group = create_vector(r_coords, YELLOW, "\\vec{r}", RIGHT + DOWN)
        vec_s_group = create_vector(s_coords, BLUE, "\\vec{s}", LEFT)

        self.play(Create(vec_r_group), Create(vec_s_group))

        show_component_breakdown(vec_r_group, r_coords, YELLOW, UR)
        show_component_breakdown(vec_s_group, s_coords, BLUE, UL)

        sub_concept = MathTex("\\vec{r} - \\vec{s} = \\vec{r} + (-1)\\vec{s}")
        bg_sub = SurroundingRectangle(sub_concept, color=WHITE, fill_color=BLACK, fill_opacity=0.8)
        sub_group = VGroup(bg_sub, sub_concept)
        sub_group.add_updater(lambda m: m.move_to(self.camera.frame.get_corner(UR) + DOWN * 2 + LEFT * 4))
        self.play(Write(sub_group))

        
        neg_s_coords = [1, -2, 0]
        vec_neg_s_final = Vector(neg_s_coords, color=RED, stroke_width=6, tip_length=0.25)
        label_neg_s = MathTex("-\\vec{s}", color=RED).next_to(vec_neg_s_final.get_end(),
                                                              RIGHT).add_background_rectangle(BLACK, 0.7)

        original_s_ghost = vec_s_group[0].copy().set_color(BLUE).set_opacity(0.3)
        self.add(original_s_ghost)

        self.play(
            vec_s_group[0].animate.become(vec_neg_s_final),
            Transform(vec_s_group[1], label_neg_s)
        )
        self.wait(0.5)

        
        self.play(vec_s_group.animate.shift(vec_r_group[0].get_end()))
        self.play(Flash(vec_r.get_end(), color=WHITE, flash_radius=0.5, run_time=0.5))

        
        final_sub_coords = [4, 0, 0]
        vec_sub_result = Vector(final_sub_coords, color=GREEN, stroke_width=6, tip_length=0.25)
        label_sub = MathTex("\\vec{r} - \\vec{s}", color=GREEN).next_to(vec_sub_result.get_end(),
                                                                        DOWN).add_background_rectangle(BLACK, 0.7)

        self.play(GrowArrow(vec_sub_result))
        self.play(Write(label_sub))
        self.play(
            Flash(vec_sub_result.get_end(), color=GREEN),
            Wiggle(label_sub)
        )

        show_component_breakdown(vec_sub_result, final_sub_coords, GREEN, UR)

        final_eq = MathTex(
            "\\begin{bmatrix} 3 \\\\ 2 \\end{bmatrix}",
            "-",
            "\\begin{bmatrix} -1 \\\\ 2 \\end{bmatrix}",
            "=",
            "\\begin{bmatrix} 4 \\\\ 0 \\end{bmatrix}"
        )
        final_eq[0].set_color(YELLOW)
        final_eq[2].set_color(BLUE)
        final_eq[4].set_color(GREEN)

        bg_final = SurroundingRectangle(final_eq, color=WHITE, fill_color=BLACK, fill_opacity=0.8)
        final_group = VGroup(bg_final, final_eq)
        final_group.add_updater(lambda m: m.move_to(self.camera.frame.get_corner(UR) + DOWN * 4 + LEFT * 4))

        self.play(FadeIn(final_group))

        self.play(Circumscribe(final_eq, color=WHITE, fade_out=True, run_time=2))
        self.play(FadeOut(original_s_ghost))

        self.wait(3)