import 'package:flutter/material.dart';
import 'package:mobile/slider_screen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Raspberry PI 5 PWM Motor',
      theme: ThemeData(
        brightness: Brightness.dark,
      ),
      home: const SliderScreenWidget(),
    );
  }
}
