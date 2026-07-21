import { useState } from "react";
import { Search } from "lucide-react";

import api from "../services/api";

import GlowBackground from "../components/ui/GlowBackground";
import GlassCard from "../components/ui/GlassCard";
import PriceChartCard from "../components/cards/PriceChartCard";
import MarketCard from "../components/cards/MarketCard";
import TechnicalCard from "../components/cards/TechnicalCard";
import NewsCard from "../components/cards/NewsCard";
import AnalysisCard from "../components/cards/AnalysisCard";
import RiskCard from "../components/cards/RiskCard";
import ReflectionCard from "../components/cards/ReflectionCard";
import ReportCard from "../components/cards/ReportCard";

function Dashboard() {
    const [ticker, setTicker] = useState("");

    const [query, setQuery] = useState("");
    const [loading, setLoading] = useState(false);

    const [market, setMarket] = useState(null);

    const [technical, setTechnical] = useState(null);
    const [history, setHistory] = useState([]);
    const [news, setNews] = useState("");
    const [analysis, setAnalysis] = useState("");
    const [risk, setRisk] = useState(null);
    const [reflection, setReflection] = useState(null);
    const [report, setReport] = useState("");

    const analyzeStock = async () => {

        if (!ticker || !query) return;

        try {

            setLoading(true);
            setMarket(null);
            setTechnical(null);
            setHistory([]);
            setNews("");
            setAnalysis("");
            setRisk(null);
            setReflection(null);
            setReport("");

            const response = await api.post(
            "/stock/analyze",
            {
                ticker,
                query
            }
            );

            setMarket(response.data.market);
            setTechnical(response.data.technical);
            setHistory(response.data.history);
            setNews(response.data.news);
            setAnalysis(response.data.analysis);
            setRisk(response.data.risk);
            setReflection(response.data.reflection);
            setReport(response.data.report);

        }

        catch (error) {

            console.error(error);

        }

        finally {

            setLoading(false);

        }

    };

    return (
    <>
        <GlowBackground />

        <main className="min-h-screen text-white px-8 py-8">

        {/* Header */}
        <div className="mb-10">
            <h1 className="text-5xl font-bold">
            ASCENT AI
            </h1>

            <p className="mt-2 text-slate-400">
            Multi-Agent Stock Analysis Platform
            </p>
        </div>

        {/* Search */}
        <GlassCard className="mb-8">

            <div className="flex flex-col gap-5">

                <div>
                <h2 className="text-2xl font-semibold">
                    Analyze a Stock
                </h2>

                <p className="mt-1 text-slate-400">
                    Ask ASCENT AI to analyze any stock using multiple AI agents.
                </p>
                </div>

                <div className="grid grid-cols-12 gap-4">

                <input
                    type="text"
                    value={ticker}
                    onChange={(e) => setTicker(e.target.value.toUpperCase())}
                    placeholder="Ticker (AAPL)"
                    className="
                    col-span-2
                    rounded-xl
                    border
                    border-white/10
                    bg-white/5
                    px-4
                    py-3
                    outline-none
                    transition
                    focus:border-cyan-400
                    "
                />

                <input
                    type="text"
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    placeholder="Analyze Apple completely..."
                    className="
                    col-span-8
                    rounded-xl
                    border
                    border-white/10
                    bg-white/5
                    px-4
                    py-3
                    outline-none
                    transition
                    focus:border-cyan-400
                    "
                />

                <button
                    onClick={analyzeStock}
                    disabled={loading}
                    className="
                    col-span-2
                    rounded-xl
                    bg-white
                    text-black
                    font-semibold
                    transition-all
                    duration-300
                    hover:scale-[1.01]
                    hover:shadow-xl
                    active:scale-95
                    flex
                    items-center
                    justify-center
                    gap-2
                    "
                >
                    {loading ? (
                        <>
                            <div className="w-4 h-4 border-2 border-black border-t-transparent rounded-full animate-spin" />
                            Analyzing...
                        </>
                    ) : (
                        <>
                            <Search size={18} />
                            Analyze
                        </>
                    )}
                </button>

                </div>

            </div>

        </GlassCard>

        {/* Market + Technical */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">

            <MarketCard
                market={market}
            />

            <TechnicalCard
                technical={technical}
            />

        </div>

        {/* Remaining Pipeline */}
        <div className="space-y-6">

            <PriceChartCard
                history={history}
            />

            <NewsCard
                news={news}
            />

            <AnalysisCard
                analysis={analysis}
            />

            <RiskCard
                risk={risk}
            />

            <ReflectionCard
                reflection={reflection}
            />

            <ReportCard
                report={report}
            />

        </div>

        </main>
    </>
    );
}

export default Dashboard;