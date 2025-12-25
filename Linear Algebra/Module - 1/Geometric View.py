from manim import *


class VectorExplanation(ThreeDScene):
    def construct(self):
        
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)

        
        HOUSE_COLOR = "
        ROOF_COLOR = "
        SHOP_COLOR = "
        VECTOR_COLOR = "
        TEXT_COLOR = WHITE
        GRID_COLOR = "
        BACKGROUND = BLACK

        
        title = Title("What is a Vector?", color=TEXT_COLOR).scale(0.9)
        underline = Line(LEFT, RIGHT, color=VECTOR_COLOR).next_to(title, DOWN)
        self.play(Write(title), Create(underline))
        self.wait(1)

        
        

        
        start_pos = ORIGIN + DOWN * 1.5 + LEFT * 2.5
        target_pos = start_pos + np.array([5, 3, 0])

        
        house = self.create_detailed_house(HOUSE_COLOR, ROOF_COLOR).scale(0.6).move_to(start_pos)
        shop = self.create_detailed_shop(SHOP_COLOR).scale(0.6).move_to(target_pos)

        house_label = Text("Home", font="Arial", font_size=24).next_to(house, DOWN, buff=0.2)
        shop_label = Text("Shop", font="Arial", font_size=24).next_to(shop, DOWN, buff=0.2)

        self.play(
            FadeIn(house, shift=UP),
            Write(house_label)
        )
        self.wait(0.3)
        self.play(
            FadeIn(shop, shift=UP),
            Write(shop_label)
        )
        self.wait(1)

        self.play(FadeOut(title), FadeOut(underline))

        
        

        
        traveler = Dot(color=VECTOR_COLOR, radius=0.08).move_to(start_pos)
        path = Line(start_pos, target_pos, color=VECTOR_COLOR, stroke_opacity=0.5)

        self.add(traveler)
        self.play(MoveAlongPath(traveler, path), run_time=2, rate_func=linear)
        self.play(traveler.animate.scale(1.5).set_color(WHITE))  
        self.play(FadeOut(traveler))

        
        vector_arrow = Arrow(start_pos, target_pos, buff=0, color=VECTOR_COLOR, stroke_width=6,
                             max_tip_length_to_length_ratio=0.15)
        vector_label = MathTex(r"\vec{v}", color=VECTOR_COLOR, font_size=48).next_to(vector_arrow.get_center(), UP,
                                                                                     buff=0.2)

        self.play(GrowArrow(vector_arrow))
        self.play(Write(vector_label))

        
        
        ref_line = DashedLine(start_pos, start_pos + RIGHT * 2, color=GRAY)
        angle = Angle(ref_line, vector_arrow, radius=0.6, color=RED)
        angle_label = MathTex(r"\theta", color=RED).next_to(angle, RIGHT, buff=0.05)

        distance_label = Text("Distance", font_size=20, color=YELLOW).next_to(vector_arrow.get_center(), DOWN,
                                                                              buff=0.2).rotate(vector_arrow.get_angle())

        self.play(Create(ref_line))
        self.play(Create(angle), Write(angle_label))
        self.play(Write(distance_label))

        phys_box = SurroundingRectangle(vector_label, color=YELLOW, buff=0.1)
        phys_text = Text("Physicist View", font="Arial", font_size=32, color=YELLOW).to_corner(UL)
        phys_sub = Text("Magnitude + Direction", font="Arial", font_size=24, color=WHITE).next_to(phys_text, DOWN)

        self.play(Write(phys_text), Write(phys_sub))
        self.wait(2)

        
        self.play(
            FadeOut(angle), FadeOut(angle_label), FadeOut(ref_line),
            FadeOut(distance_label), FadeOut(phys_text), FadeOut(phys_sub),
            FadeOut(phys_box)
        )

        
        

        
        grid = NumberPlane(
            x_range=[-2, 8, 1],
            y_range=[-2, 6, 1],
            background_line_style={
                "stroke_color": GRID_COLOR,
                "stroke_width": 2,
                "stroke_opacity": 0.3
            }
        )
        
        
        grid.move_to(start_pos + np.array([3, 2, 0]))

        
        axes = Axes(
            x_range=[-1, 7], y_range=[-1, 5],
            x_length=8, y_length=6,
            axis_config={"include_tip": True, "color": GRAY}
        ).move_to(start_pos, aligned_edge=DL).shift(LEFT * 1 + DOWN * 1)  
        
        axes = Axes(
            x_range=[0, 6], y_range=[0, 4],
            x_length=6, y_length=4,
            axis_config={"include_tip": True, "color": GRAY}
        )
        
        axes.next_to(start_pos, UP + RIGHT, buff=0).shift(
            DOWN * axes.y_axis.get_length() / 2 * 0 + LEFT * axes.x_axis.get_length() / 2 * 0)
        
        axes.move_to(start_pos, aligned_edge=DL)

        self.play(Create(grid, run_time=2), FadeIn(axes))

        
        
        x_path = Line(start_pos, start_pos + RIGHT * 5, color=RED, stroke_width=4)
        x_label = MathTex("x = 5", color=RED).next_to(x_path, DOWN)
        x_dot = Dot(color=RED).move_to(start_pos)

        self.play(MoveAlongPath(x_dot, x_path), ShowPassingFlash(x_path.copy().set_color(RED), time_width=0.5))
        self.add(x_path)
        self.play(Write(x_label))

        
        y_path = Line(start_pos + RIGHT * 5, target_pos, color=GREEN, stroke_width=4)
        y_label = MathTex("y = 3", color=GREEN).next_to(y_path, RIGHT)
        y_dot = Dot(color=GREEN).move_to(start_pos + RIGHT * 5)

        self.play(MoveAlongPath(y_dot, y_path), ShowPassingFlash(y_path.copy().set_color(GREEN), time_width=0.5))
        self.add(y_path)
        self.play(Write(y_label))

        self.remove(x_dot, y_dot)

        
        coord_matrix = MathTex(r"\begin{bmatrix} 5 \\ 3 \end{bmatrix}", color=BLUE, font_size=48).next_to(shop, UP)

        cs_text = Text("CS Student View", font="Arial", font_size=32, color=BLUE).to_corner(UL)
        cs_sub = Text("Array of Numbers", font="Arial", font_size=24, color=WHITE).next_to(cs_text, DOWN)

        self.play(Write(cs_text), Write(cs_sub))
        self.play(TransformFromCopy(VGroup(x_label, y_label), coord_matrix))
        self.wait(2)

        
        

        self.play(
            FadeOut(cs_text), FadeOut(cs_sub),
            FadeOut(x_label), FadeOut(y_label),
            FadeOut(x_path), FadeOut(y_path),
            FadeOut(coord_matrix),
            FadeOut(grid), FadeOut(axes),
            FadeOut(vector_label)
        )

        
        building_height = 3.5
        building = self.create_detailed_building(SHOP_COLOR, height=building_height)
        building.move_to(target_pos + OUT * building_height / 2)

        
        
        self.move_camera(
            phi=60 * DEGREES,
            theta=-45 * DEGREES,
            added_anims=[
                FadeOut(shop),
                FadeOut(shop_label),
                GrowFromCenter(building)
            ],
            run_time=3
        )

        
        building_text = Text("50 Floors", font="Arial", font_size=24, color=WHITE)
        building_text.rotate(90 * DEGREES, axis=RIGHT)
        building_text.rotate(90 * DEGREES, axis=OUT)
        building_text.next_to(building, RIGHT, buff=0.5)
        self.play(Write(building_text))

        
        new_target = target_pos + OUT * (building_height - 0.5)  

        vector_3d = Arrow3D(
            start=start_pos,
            end=new_target,
            color=VECTOR_COLOR
        )

        
        line_x = Line3D(start=start_pos, end=start_pos + RIGHT * 5, color=RED)
        line_y = Line3D(start=start_pos + RIGHT * 5, end=start_pos + RIGHT * 5 + UP * 3, color=GREEN)
        line_z = Line3D(start=start_pos + RIGHT * 5 + UP * 3, end=new_target, color=BLUE)

        self.play(Transform(vector_arrow, vector_3d), run_time=1.5)
        self.play(
            Create(line_x),
            Create(line_y),
            Create(line_z),
            run_time=1.5
        )

        
        final_matrix = MathTex(r"\begin{bmatrix} 5 \\ 3 \\ \text{Floor} \end{bmatrix}", color=GOLD)
        final_matrix.to_corner(UR)

        self.add_fixed_in_frame_mobjects(final_matrix)
        self.play(Write(final_matrix))

        self.wait(2)

        
        pass_text = Text("Vectors encode Multidimensional Data", font="Arial", font_size=36, gradient=(BLUE, YELLOW))
        pass_text.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(pass_text)
        self.play(Write(pass_text))
        self.wait(3)

    

    def create_detailed_house(self, color, roof_color):
        
        base = Square(side_length=1, fill_color=color, fill_opacity=1, stroke_color=WHITE, stroke_width=2)

        
        roof = Polygon(
            [-0.6, 0.5, 0], [0.6, 0.5, 0], [0, 1.1, 0],
            fill_color=roof_color, fill_opacity=1, stroke_color=WHITE, stroke_width=2
        )

        
        door = Rectangle(width=0.3, height=0.5, fill_color="
                         stroke_width=1)
        door.move_to(base.get_bottom() + UP * 0.25)

        
        window = Square(side_length=0.3, fill_color="
        window.move_to(base.get_top() + DOWN * 0.3)
        window_cross_v = Line(window.get_top(), window.get_bottom(), color=WHITE, stroke_width=1)
        window_cross_h = Line(window.get_left(), window.get_right(), color=WHITE, stroke_width=1)

        return VGroup(base, roof, door, window, window_cross_v, window_cross_h)

    def create_detailed_shop(self, color):
        
        base = Rectangle(width=1.4, height=1, fill_color=color, fill_opacity=1, stroke_color=WHITE, stroke_width=2)

        
        canopy = VGroup()
        for i in range(5):
            c_color = RED if i % 2 == 0 else WHITE
            strip = Rectangle(width=1.4 / 5, height=0.3, fill_color=c_color, fill_opacity=1, stroke_width=0)
            strip.move_to(np.array([-0.7 + (1.4 / 10) + i * (1.4 / 5), 0.65, 0]))
            canopy.add(strip)

        
        window = Rectangle(width=1.0, height=0.5, fill_color="
        window.move_to(base.get_center() + UP * 0.1)
        reflection = Line(window.get_corner(DL), window.get_corner(UR), color=WHITE, stroke_width=1, stroke_opacity=0.5)

        text = Text("SHOP", font_size=12, color=WHITE, weight=BOLD).next_to(canopy, UP, buff=0.05)

        return VGroup(base, canopy, window, reflection, text)

    def create_detailed_building(self, color, height=3):
        
        building = Prism(dimensions=[1.2, 1.2, height], fill_color=color, fill_opacity=0.8)

        
        lines = VGroup()
        for h in np.linspace(-height / 2 + 0.2, height / 2 - 0.2, 10):
            lines.add(
                Line3D(start=[-0.6, -0.6, h], end=[0.6, -0.6, h], color=WHITE),
                Line3D(start=[0.6, -0.6, h], end=[0.6, 0.6, h], color=WHITE),
            )

        return VGroup(building, lines)