import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Cell } from 'recharts';

interface EmotionChartProps {
  probabilities: number[];
}

export function EmotionChart({ probabilities }: EmotionChartProps) {
  const emotions = ["neutral", "angry", "happy", "sad"];
  const colors = ["#64748b", "#ef4444", "#f59e0b", "#3b82f6"];
  
  const data = emotions.map((emotion, index) => ({
    emotion,
    probability: probabilities[index] * 100, // 转换为百分比
    fill: colors[index]
  }));

  console.log('Rendering EmotionChart with data:', data);

  return (
    <div className="w-full" style={{ height: '300px' }}>
      <ResponsiveContainer width="100%" height="100%">
        <BarChart
          data={data}
          margin={{
            top: 20,
            right: 30,
            left: 20,
            bottom: 5,
          }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis 
            dataKey="emotion" 
            label={{ 
              value: 'Emotions', 
              position: 'bottom', 
              offset: 10 // 调整偏移量以避免文字被遮挡
            }}
          />
          <YAxis
            label={{ 
              value: 'Probability (%)', 
              angle: -90, 
              position: 'insideLeft',
              offset: 10
            }}
          />
          <Tooltip 
            formatter={(value: number) => `${value.toFixed(1)}%`}
            contentStyle={{
              backgroundColor: 'rgba(255, 255, 255, 0.95)',
              border: '1px solid #ccc',
              borderRadius: '6px'
            }}
          />
          <Bar 
            dataKey="probability" 
            radius={[4, 4, 0, 0]}
            animationDuration={1000}
          >
            {data.map((entry, index) => (
              <Cell key={`cell-${index}`} fill={entry.fill} />
            ))}
          </Bar>
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
