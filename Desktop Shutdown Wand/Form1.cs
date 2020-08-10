using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Desktop_Wand
{
    public partial class Desktop_Shutdown_Wand : Form
    {
        long Timer;
        public Desktop_Shutdown_Wand()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void Button_Click(object sender, EventArgs e)
        {
            Button newbie = (Button)sender;
            Timer = newbie.TabIndex;
            Timer_Text.Text = "There will be a shutdown in      " + Timer.ToString() + " second(s)."; 
        }

        private void Button_Click2(object sender, EventArgs e)
        {
            if (comboBox1.Text == "Minute(s)")
            {
                Timer = Convert.ToInt64(scale.Value * 60);
            }
            else if (comboBox1.Text == "Hour(s)")
            {
                Timer = Convert.ToInt64(scale.Value * 3600);
            }
            else
            {

            }
            Timer_Text.Text = "There will be a shutdown in      " + Timer.ToString() + " second(s).";
        }

        private void button11_Click(object sender, EventArgs e)
        {
            String exe_Text = "shutdown -s -t " + Timer;
            System.Diagnostics.Process process = new System.Diagnostics.Process();
            System.Diagnostics.ProcessStartInfo startInfo = new System.Diagnostics.ProcessStartInfo();
            startInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden;
            startInfo.FileName = "cmd.exe";
            startInfo.Arguments = "/C " + exe_Text;
            process.StartInfo = startInfo;
            process.Start();
        }

        private void button14_Click(object sender, EventArgs e)
        {
            System.Diagnostics.Process process = new System.Diagnostics.Process();
            System.Diagnostics.ProcessStartInfo startInfo = new System.Diagnostics.ProcessStartInfo();
            startInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden;
            startInfo.FileName = "cmd.exe";
            startInfo.Arguments = "/C shutdown -a";
            process.StartInfo = startInfo;
            process.Start();
        }
    }
}
