import 'package:flutter/material.dart';

void main() {
  runApp(GHPlusApp());
}

class GHPlusApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'GH_PLUS',
      theme: ThemeData(
        primarySwatch: Colors.deepPurple,
      ),
      home: WelcomeScreen(),
    );
  }
}

class WelcomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.deepPurple[50],
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(32.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Icon(Icons.code, size: 80, color: Colors.deepPurple),
              SizedBox(height: 20),
              Text(
                'Bienvenido a GH_PLUS',
                style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
              ),
              SizedBox(height: 20),
              Text(
                'Gestioná tus Codespaces y comandos desde el móvil.',
                textAlign: TextAlign.center,
              ),
              SizedBox(height: 40),
              ElevatedButton.icon(
                icon: Icon(Icons.login),
                label: Text('Iniciar sesión con GitHub'),
                onPressed: () {
                  // TODO: Implementar flujo OAuth
                },
              ),
            ],
          ),
        ),
      ),
    );
  }
}
