package com.kimo.activities;


import android.content.Intent;
import android.os.StrictMode;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.example.demo.R;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.ProtocolException;
import java.net.URL;

public class MainActivity extends AppCompatActivity {
    EditText eText;
    Button btn;
    Button nextActivity;
    public static final String MESSAGE = "MESSAGE";
    public boolean validat=false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
        StrictMode.setThreadPolicy(policy);

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        eText = (EditText) findViewById(R.id.edittext);
        btn = (Button) findViewById(R.id.button);
        nextActivity = (Button) findViewById(R.id.button2);

        try{
            FileInputStream fIn = openFileInput("filename.txt");
            InputStreamReader isr = new InputStreamReader(fIn);
            char[] inputBuffer = new char[6];
            //len is the length of that saved string in the file

            isr.read(inputBuffer);

            String readString = new String(inputBuffer);
            System.out.println(readString);
            if (!readString.equals("")){
                Intent intent = new Intent(getApplicationContext(), SecondActivity.class);
                intent.putExtra(MESSAGE, readString);
                startActivity(intent);
            }
        }catch(IOException e){

        }







        btn.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {

                    try{
                        String text = eText.getText().toString();
                        FileOutputStream fOut = openFileOutput("filename.txt",MODE_WORLD_READABLE);
                        OutputStreamWriter osw = new OutputStreamWriter(fOut);
                        osw.write(text);
                        osw.flush();
                        osw.close();
                        validat=true;
                    }catch(IOException ioe){
                    }

            }
        });

        nextActivity.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                if(validat==false){
                    Snackbar snackbar = Snackbar.make(v, "Validati mai intai token-ul", Snackbar.LENGTH_LONG);
                    snackbar.show();
                }
                else {
                    String str = eText.getText().toString();
                    Intent intent = new Intent(getApplicationContext(), SecondActivity.class);
                    intent.putExtra(MESSAGE, str);
                    startActivity(intent);
                }
            }
        });
    }
}
