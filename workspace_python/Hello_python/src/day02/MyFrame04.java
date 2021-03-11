package day02;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JButton;
import java.awt.BorderLayout;
import javax.swing.JTextField;
import javax.swing.JLabel;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyFrame04 {

	private JFrame frame;
	private JTextField tf1;
	private JTextField tf2;
	private JTextField tf3;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyFrame04 window = new MyFrame04();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public MyFrame04() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frame = new JFrame();
		frame.setBounds(100, 100, 450, 300);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setLayout(null);
		
		JLabel lblNewLabel = new JLabel("\uC5D0\uC11C");
		lblNewLabel.setBounds(56, 47, 37, 15);
		frame.getContentPane().add(lblNewLabel);
		
		tf1 = new JTextField();
		tf1.setBounds(12, 45, 43, 18);
		frame.getContentPane().add(tf1);
		tf1.setColumns(10);
		
		JButton btn = new JButton("\uAE4C\uC9C0\uC758\uD569");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int sum = 0;
				for(int i=Integer.valueOf(tf1.getText());i <=Integer.valueOf(tf2.getText()); i++ )
				{
					sum += i ;
				}
				tf3.setText(String.valueOf(sum));
				
			}
		});
		
		
		btn.setBounds(135, 45, 89, 19);
		frame.getContentPane().add(btn);
		
		tf2 = new JTextField();
		tf2.setColumns(10);
		tf2.setBounds(87, 45, 43, 18);
		frame.getContentPane().add(tf2);
		
		tf3 = new JTextField();
		tf3.setColumns(10);
		tf3.setBounds(232, 45, 43, 18);
		frame.getContentPane().add(tf3);
	}

}
