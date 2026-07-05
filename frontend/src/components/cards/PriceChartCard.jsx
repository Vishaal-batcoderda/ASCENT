
import { useState } from "react";

import GlassCard from "../ui/GlassCard";

import {
    ResponsiveContainer,
    LineChart,
    Line,
    XAxis,
    YAxis,
    Tooltip,
    CartesianGrid
} from "recharts";

function PriceChartCard({history}) {

    const [selectedPeriod, setSelectedPeriod] = useState("6M");

    if (!history || history.length === 0) {

        return (

            <GlassCard className="mb-6">

                <h2 className="text-xl font-semibold mb-5">
                    Price History
                </h2>

                <p className="text-slate-500">
                    Analyze a stock to view its price chart.
                </p>

            </GlassCard>

        );

    }
    
    const latestPrice = history[history.length - 1]?.Close;

    let filteredHistory = history;

    switch (selectedPeriod) {

        case "1M":
            filteredHistory = history.slice(-22);
            break;

        case "3M":
            filteredHistory = history.slice(-66);
            break;

        case "6M":
        default:
            filteredHistory = history;
    }

    const chartData = filteredHistory.map((item) => ({
        date: new Date(item.Date).toLocaleDateString(
            "en-US",
            {
                month: "short",
                day: "numeric",
            }
        ),
        close: item.Close,
    }));

    return (
        <GlassCard className="mb-6">
            <div className="flex items-center justify-between mb-5">

                <h2 className="text-xl font-semibold">
                    Price History
                </h2>

                <div className="flex gap-2">

                    {
                        ["1M", "3M", "6M"].map((period) => (

                            <button
                                key={period}
                                onClick={() => setSelectedPeriod(period)}
                                className={`
                                    px-3
                                    py-1
                                    rounded-lg
                                    text-sm
                                    transition-all
                                    duration-150

                                    ${
                                        selectedPeriod === period

                                        ?

                                        "bg-white text-black"

                                        :

                                        "bg-white/5 text-slate-300 hover:bg-white/10"
                                    }
                                `}
                            >
                                {period}
                            </button>

                        ))

                    }

                </div>

            </div>

            <div className="mb-4">

                    <p className="text-3xl font-bold">
                        ${latestPrice?.toFixed(2)}
                    </p>

                    <p className="text-slate-400 text-sm">
                        Latest Closing Price
                    </p>

            </div>
            
            <ResponsiveContainer
                width="100%"
                height={350}
            >
                
                <LineChart data={chartData}>

                    <CartesianGrid
                        stroke="#1e293b"
                        strokeDasharray="4 4"
                        vertical={false}
                    />

                    <XAxis
                        dataKey="date"
                        tick={{
                            fill: "#94a3b8",
                            fontSize: 12,
                        }}
                        tickMargin={10}
                        minTickGap={35}
                        tickLine={false}
                        axisLine={false}
                    />

                    <YAxis
                        domain={["auto", "auto"]}
                        tick={{
                            fill: "#94a3b8",
                            fontSize: 12,
                        }}
                        tickFormatter={(value) => `$${value.toFixed(0)}`}
                        tickLine={false}
                        axisLine={false}
                    />

                    <Tooltip
                        contentStyle={{
                            backgroundColor: "#0f172a",
                            border: "1px solid #334155",
                            borderRadius: "12px",
                        }}
                        labelStyle={{
                            color: "#ffffff",
                        }}
                    />

                    <Line
                        type="monotone"
                        dataKey="close"
                        stroke="#38bdf8"
                        strokeWidth={3}
                        dot={false}
                        activeDot={{
                            r: 6,
                        }}
                        animationDuration={800}
                    />

                </LineChart>

            </ResponsiveContainer>
        
        </GlassCard>
    );

}

export default PriceChartCard;