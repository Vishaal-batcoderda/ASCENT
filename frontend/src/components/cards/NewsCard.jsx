import ReactMarkdown from "react-markdown";
import GlassCard from "../ui/GlassCard";

function NewsCard({ news }) {

    return (

        <GlassCard>

            <h2 className="text-xl font-semibold mb-5">
                News Summary
            </h2>

            {
                news ? (

                    <article
                        className="
                            prose
                            prose-invert
                            max-w-none
                            prose-headings:text-white
                            prose-p:text-slate-300
                            prose-strong:text-white
                            prose-li:text-slate-300
                            prose-ul:my-2
                            prose-p:leading-7
                        "
                    >

                        <ReactMarkdown>

                            {news}

                        </ReactMarkdown>

                    </article>

                ) : (

                    <p className="text-slate-500">
                        Analyze a stock to view the latest news summary.
                    </p>

                )

            }

        </GlassCard>

    );

}

export default NewsCard;